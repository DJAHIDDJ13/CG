(ns Player
  (:require [clojure.string :as str])
  (:gen-class))

; Auto-generated code below aims at helping you parse
; the standard input according to the problem statement.

(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (let [; the number of points used to draw the surface of Mars.
        surfaceN (Integer/parseInt (read-line))]
    (loop [i surfaceN]
      (when (> i 0)
        (let [; landX: X coordinate of a surface point. (0 to 6999)
              ; landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
              [landX landY] (map #(Integer/parseInt %) (str/split (read-line) #" "))]
        (recur (dec i)))))
    (while true
      (let [; hSpeed: the horizontal speed (in m/s), can be negative.
            ; vSpeed: the vertical speed (in m/s), can be negative.
            ; fuel: the quantity of remaining fuel in liters.
            ; rotate: the rotation angle in degrees (-90 to 90).
            ; power: the thrust power (0 to 4).
            [X Y hSpeed vSpeed fuel rotate power] (map #(Integer/parseInt %) (str/split (read-line) #" "))]
        
        ; (debug "Debug messages...")
        
        ; 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
        (output "0 4")
        (output "0 3")))))