#!/usr/bin/env python  
import roslib
roslib.load_manifest('sufrimiento_semestral')
import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import PointCloud
import csv

def cmd_velReceived(message):
    with open('training.csv', 'a') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([message.linear.x,message.linear.y, message.linear.z,  message.angular.x, message.angular.y, message.angular.z])
	rospy.loginfo("linear x %f", message.linear.x)
	rospy.loginfo("linear y %f", message.linear.y)
	rospy.loginfo("linear z %f", message.linear.z)
        rospy.loginfo("angual x %f", message.angular.x)
	rospy.loginfo("angular y %f", message.angular.y)
	rospy.loginfo("angular z %f", message.angular.z)
	
def leftSensorCallback(data):
 with open('trainingSensorL.csv', 'a') as csv:
     spamwriter = csv.writer(csv, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow([data.points[0].x])
     leftDistance = data.points[0].x
     rospy.loginfo("SENSOR IZQUIERDA x %f", data.points[0].x)


def rightSensorCallback(data):
 with open('trainingSensorR.csv', 'a') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow([data.points[0].x])
     rightDistance = data.points[0].x
     rospy.loginfo("SENSOR DERECHO x %f", data.points[0].x)


def floorSensorCallback(data):
 with open('trainingSensorF.csv', 'a') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow([data.points[0].x])
     floorDistance = data.points[0].x
     rospy.loginfo("SENSOR PISO x %f", data.points[0].x)
	

rospy.init_node('sufrimiento_semestral', log_level=rospy.DEBUG)
rospy.loginfo("Me subscribire al canal cmd_vel")
rospy.Subscriber('/cmd_vel', Twist, cmd_velReceived)
rospy.Subscriber('/distance_sensors_state/front_left_srf10', PointCloud, leftSensorCallback)
rospy.Subscriber('/distance_sensors_state/front_right_srf10', PointCloud, rightSensorCallback)
rospy.Subscriber('/distance_sensors_state/floor_sensor', PointCloud, floorSensorCallback)

rospy.spin()

	
