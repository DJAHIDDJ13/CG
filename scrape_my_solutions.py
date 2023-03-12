import codecs
import datetime
import os
import time
import requests
import json
from markdownify import markdownify

# Might need to change this dict since i didn't test them all
language_to_extension = {
    "Bash": ".sh",
    "C": ".c",
    "C#": ".cs",
    "C++": ".cpp",
    "Clojure": ".clj",
    "D": ".d",
    "Dart": ".dart",
    "F#": ".fs",
    "Go": ".go",
    "Groovy": ".groovy",
    "Haskell": ".hs",
    "Java": ".java",
    "Javascript": ".js",
    "Kotlin": ".kt",
    "Lua": ".lua",
    "ObjectiveC": ".m",
    "OCaml": ".ml",
    "Pascal": ".pas",
    "Perl": ".pl",
    "PHP": ".php",
    "Python3": ".py",
    "Ruby": ".rb",
    "Rust": ".rs",
    "Scala": ".scala",
    "Swift": ".swift",
    "TypeScript": ".ts",
    "VB.NET": ".vb"
}

# rememberMe cookie can be found in your browser's devtools 
cookies = {
    'rememberMe': '<PUT YOUR REMEMBERME COOKIE HERE>'
}

# TODO: Handle status code 422, {"id":558,"message":"Solutions are not available for this puzzle"}
def req(service, data):
    response = requests.post(
       f'https://www.codingame.com/services/{service}',
        cookies=cookies,
        json=data,
    )

    if response.status_code != 200:
        print(response.content)
        raise Exception(f"Request failed with status code {response.status_code}: {response.reason}")

    content = json.loads(response.content)
    return content

# You can grab your handle from the url of your profile
data = ['<PUT YOUR PROFILE HANDLE HERE>']
res = req("CodinGamer/findCodingamePointsStatsByHandle", data)
user_id = res['codingamer']['userId']
time.sleep(1)


print(user_id)

data = [user_id]
all_puzzles = req("Puzzle/findAllMinimalProgress", data)
time.sleep(1)

solved_puzzle_ids = [puzzle['id'] for puzzle in all_puzzles if puzzle['validatorScore'] == 100] 
data = [solved_puzzle_ids, user_id, 2]
solved_puzzles = req("Puzzle/findProgressByIds", data)

for j, puzzle in enumerate(solved_puzzles[114:]):
    print(f"[{j:03d}/{len(solved_puzzles):03d}]{puzzle['prettyId']}")
    data = [puzzle['prettyId'], user_id]
    puzzle_info = req("Puzzle/findProgressByPrettyId", data)
    time.sleep(.2)
    out_dir = puzzle['detailsPageUrl'][1:] # probably a bad idea to do it like this but meh
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    data = [user_id, puzzle_info['id'], None] # last arg null to get all languages
    my_solutions = req('Solution/findMySolutions', data)
    time.sleep(.2)

    table_header = "| filename | Language | Submission date |\n| --- | --- | --- |\n"
    solution_log_table = [table_header]
    for i, solution in enumerate(my_solutions):
        language = solution['programmingLanguageId']
        date = datetime.datetime.fromtimestamp(solution['creationTime']/1000)
        date = date.strftime("%Y-%m-%d %a %H:%M")
        extension = language_to_extension[language]
        fname = f"solution_{i}{extension}"
        with codecs.open(os.path.join(out_dir, fname), 'w', encoding='utf-8') as f:
            f.write(solution['code'])
        solution_log_table.append(f"| {fname} | {language} | {date} |\n")


    with codecs.open(os.path.join(out_dir, "README.md"), "w", encoding='utf-8') as f:
        url = f"https://www.codingame.com{puzzle['detailsPageUrl']}"
        f.write(f"# {puzzle['title']} \[[link]({url})\]\n")
        if 'description' in puzzle_info:
            f.write("## Problem Description:\n")
            f.write(puzzle_info['description'])
            f.write("\n")
        f.write(markdownify(puzzle_info['statement']))
        f.write("\nSolutions:\n")
        f.write("".join(solution_log_table))