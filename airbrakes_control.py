import numpy
from serial import Serial

# Error terms
error_1 = 0
error_2 = 0
error_3 = 0


class SensorData:

    """
    A container class for all of the sensor data being recieved from the main flight computer program
    """

    def __init__(self, a, b, c, d, e, f):
        # TODO check what actual sensors are being used and rename the a, b, c etc placeholders with actual sensor names
        self.sensor_data = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f}

    def sensor_values(self):
        return self.sensor_data

    def get_sensor_values(self, sensor_values):
        for i in sensor_values:
            self.sensor_data[i] = sensor_values[i]


class SystemState:

    """
        A matrix representation of state of the rocket generated from SensorData class
    """

    def __init__(self, state_matrix, covariance_matrix, u, w, q):
        """
        Creates the System state object
        :param state_matrix: A matrix representation of the rockets state
        :param covariance_matrix: A matrix of covariance terms used by the Kalman filter
        :param u: Error term
        :param w: Error term
        :param q: Error term
        """
        self.state_matrix = state_matrix
        self.covariance_matrix = covariance_matrix
        self.u = u
        self.w = w
        self.q = q

    def get_state_matrix(self):
        return self.state_matrix

    def get_covariance_matrix(self):
        return self.covariance_matrix

    def set_state_matrix(self, state_matrix):
        self.state_matrix = state_matrix

    def set_covariance_matrix(self, covariance_matrix):
        self.covariance_matrix = covariance_matrix


def generate_state_matrix(sensor_data):
    pass
    # TODO consult math person this is too hard


def generate_covariance_matrix(sensor_data):
    pass
    # TODO consult math person this is too hard


def predict(system_state):
    pass

    """
    recursive function taking sensor data and running it through an algorithm to get next possible sensor data
    best to use changes in sensor data (acceleration, velocity)
    
    are we getting acceleration component-wise or magnitude wise? we only want to consider vertical component of
    acceleration. component-wise acceleration data would be great.
    
    Kieran's idea: instead of implementing algorithm all the way to velocity zero at 10k, implement to a certain 
    velocity at a certain height below 10k which would result in velocity zero at 10k. This is because the airbrakes
    provide negligible force at low velocities, which means implementing the kalman filter would take extra computing
    resources that are not necessary (and the math and programming for that would be more difficult to implement).
    to do this: run airbrakes code to get the rocket to a certain speed at a certain height (calculated in another
    function, or hard coded based on weight of rocket?) and then shut off the airbrakes code.
    """

    # TODO consult math person this is too hard (kalman filter)


def update(system_state, sensor_data):
    pass

    """
    this function is used to update the algorithm to account for error.
    
    let's say the kalman function makes a prediction halfway through the flight about the state of the rocket at
    3/4 of the way through the flight. at 3/4 of the way through, the sensor data would be compared with the predicted
    state and the kalman "predict" algorithm would be changed based on the difference between the two.
    
    this would be happening constantly: prediction, comparison, and algorithm improvement as the rocket runs.
    
    !!we should have the rocket self adjust to follow a pre-calculated flight path!!
    """

    # TODO consult math person this is too hard (kalman filter)


def return_airbrake_value(filtered_system_state):
    pass
    # TODO calculate desired drag force and convert that into output for airbrakes, write value to airbrakes serial


def airbrakes_control(a, b, c, d, e, f):
    """
    The function that will be called by the flight computer main program to actually control the airbrakes
    The parameters a-f are all placeholders and will be replaced with the names of the sensors from which we are
    gathering data
    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    :param f:
    :return:
    """
    sensor_data = SensorData(a, b, c, d, e, f)

    system_state = SystemState(generate_state_matrix(sensor_data), generate_covariance_matrix(sensor_data),
                               error_1, error_2, error_3)

    return_airbrake_value(predict(system_state))
    sensor_data.get_sensor_values()
    update(system_state, sensor_data)

