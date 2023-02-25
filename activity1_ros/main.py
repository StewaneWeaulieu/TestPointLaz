import sys
import rosbag
import csv

import rospy
import roslaunch


if __name__ == '__main__':

	package = 'rqt_gui'
	executable = 'rqt_gui'
	node = roslaunch.core.Node(package, executable)

	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print(process.is_alive())

	process.stop()

	exit()

	if len(sys.argv) <= 2:
		print("You need to enter the file name of the bag as the first argument and the topic as the second argument.")
		exit()

	bag_name = sys.argv[1]
	topic_name = sys.argv[2]

	bag = rosbag.Bag(bag_name)

	file = open('output.csv', 'w', newline='')
	writer = csv.writer(file)
	writer.writerow(["x", "y", "z"])

	for topic, message, time in bag.read_messages(topic_name):
		print(message)





	