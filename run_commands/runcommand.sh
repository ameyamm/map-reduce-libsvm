hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar -file /home/hduser/CSI5387_Project/src/mapper_svm.py -mapper /home/hduser/CSI5387_Project/src/mapper_svm.py  -file /home/hduser/CSI5387_Project/src/reducer_svm.py -reducer /home/hduser/CSI5387_Project/src/reducer_svm.py -input /user/hadoop/test/* -output /user/hadoop/test-output/
