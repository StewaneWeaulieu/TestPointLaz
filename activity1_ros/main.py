import sys
import rosbag

if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print("You need to enter the file name of the bag as the first argument and the topic as the second argument.")
		exit()

	bag_name = sys.argv[1]
	topic_name = sys.argv[2]

	bag = rosbag.Bag(bag_name)

	for topic, message, time in bag.read_messages(topic_name):
		print(message)




	