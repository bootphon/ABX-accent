**ABXpy score**
================

Use the ABXpy package 
Organisation
It is composed of 3 main modules and other submodules.

- `Task module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module>`_: is used for creating a new task and preprocessing.
   We used across and within tasks, each one has his own results on each folder.

- `Distance package <https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html>`_: is used for calculating the distances necessary for the score calculation.

- `Score module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module>`_: is used for computing the score of a task.

- `analyze module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module>`_: is used for analysing the results.

across task example:
======== ========= ========== =========== ============= ====== ===
phone_1	 speaker_1	 phone_2	   speaker_2	       by	     score	  n
-------- --------- ---------- ----------- ------------- ------ ---
    k	    G10208	     l	       G11139	     ('aɪ', 'aɪ')	1.0	1
======== ========= ========== =========== ============= ====== ===

within task example:

======== ========= ===================== ====== ===
phone_1	  phone_2	     by	               score	  n
-------- --------- --------------------- ------ --- 
   n        l	     ('G00473', 'aɪ', 'd')	  0.9	 30
======== ========= ===================== ====== ===
