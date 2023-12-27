import os
import launch
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController

def generate_launch_description():
    package_dir = get_package_share_directory('crazyflie_package')
    robot_description_path = os.path.join(package_dir, 'resource', 'crazyflie.urdf')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'crazy_world.wbt')
    )

    crazyflie_driver1 = WebotsController(
        robot_name='Crazyflie1',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )
    crazyflie_driver2 = WebotsController(
        robot_name='Crazyflie2',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )    
    

    return LaunchDescription([
        webots,
        crazyflie_driver1,
        crazyflie_driver2,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
