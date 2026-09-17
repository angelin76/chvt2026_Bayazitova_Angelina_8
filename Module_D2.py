import time
import rclpy
from rclpy.logging import get_logger
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from moveit.planning import MoveItPy

def plan_and_execute(moveit, planning_component, logger, sleep_time=1.0):
    logger.info("Planning...")
    plan_result = planning_component.plan()

    if plan_result:
        logger.info("Executing...")
        robot_trajectory = plan_result.trajectory
        moveit.execute(robot_trajectory, controllers=[])
    else:
        logger.error("Planning failed")

    time.sleep(sleep_time)

def main():
    rclpy.init()
    logger = get_logger("moveit_py_example")

    # Инициализация объектов MoveItPy
    arm95 = MoveItPy(node_name="moveit_py_example", name_space="/RMC1/arm95")
    # Объект - манипулятор
    arm95_arm = arm95.get_planning_component("arm95_group")
    # Объект - захват
    gripper = arm95.get_planning_component("gripper")

    logger.info("MoveItPy connected")

    # Пример открытия захвата
    gripper.set_goal_state(configuration_name="open")
    plan_and_execute(arm95, gripper, logger, sleep_time=0.0)

    # Пример закрытия захвата
    gripper.set_goal_state(configuration_name="closed")
    plan_and_execute(arm95, gripper, logger, sleep_time=0.0)


    # Пример движения манипулятора
    # Старт из текущего положения
    arm95_arm.set_start_state_to_current_state()

    # Целевая ориентация схвата в углах Эйлера относительно основания "base_link"
    # Задается в виде roll, pitch, yaw
    # Ориентация из углов Эqлера переводится в кватернион
    q = quaternion_from_euler(0.0, 0.0, 1.57)

    # Задать целевую позицию в формате PoseStamped сообщения
    pose_goal = PoseStamped()
    pose_goal.header.frame_id = "base_link"
    pose_goal.pose.orientation.x = q[0]
    pose_goal.pose.orientation.y = q[1]
    pose_goal.pose.orientation.z = q[2]
    pose_goal.pose.orientation.w = q[3]
    pose_goal.pose.position.x = 0.3
    pose_goal.pose.position.y = 0.0
    pose_goal.pose.position.z = 0.6
    arm95_arm.set_goal_state(pose_stamped_msg=pose_goal, pose_link="tcp_frame")
    plan_and_execute(arm95, arm95_arm, logger, sleep_time=0.0)

if __name__ == "__main__":
    main()