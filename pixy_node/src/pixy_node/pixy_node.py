import rospy
import math
from std_msgs.msg import UInt16
from pixy import *
from ctypes import *

def get_angle(targetX, targetY):
    # tweak orig if its not zero zero
    origX = 0
    origX = 0
    myradians = math.atan2(targetY-origX, targetX-origX)
    degrees = math.degrees(myradians)
    if degrees < 0:
        degrees = abs(degrees) + 180
    return degrees

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

def _node_setup():
    pixy_init()
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    rospy.init_node('pixy_node', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    return pub

class CyclicBoundedList(object):
    def __init__(self, max):
        self._max = max
        self._list = []
    def append(self, item):
        self._list.append(item)
        if len(self._list) > self._max:
            self._list.pop(0)
    def __getitem__(self, idx):
        return self._list[idx]
    def avg(self):
        return (sum(self._list) / len(self._list))
    def clear(self):
        self._list = []
    def is_saturated(self):
        return len(self._list) == self._max

def pixy_node():
    angle_publisher = _node_setup()
    angles = CyclicBoundedList(5)
    print 'Calling pixy_get_blocks'
    while not rospy.is_shutdown():
        blocks = BlockArray(100)
        count = pixy_get_blocks(100, blocks)
        for index in range (0, count):
            block_log = '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d ANGLE=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height, blocks[index].angle)
            print block_log
            rospy.loginfo(block_log)

            angle = get_degrees(blocks[index].x, blocks[index].y)
            angles.append(angle)
            if angles.is_saturated():
                angle_publisher.publish(int(angles.avg()))
        if count == 0:
            angles.clear()

if __name__ == '__main__':
    try:
        pixy_node()
    except rospy.ROSInterruptException:
        pass
