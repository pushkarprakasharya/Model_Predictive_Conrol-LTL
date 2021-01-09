import numpy as np


class Obstacle_Moved(Exception):
    pass


pl = np.array([  # 0-31
 [0.261532, -0.262342],
 [0.784595, -0.262342],
 [1.30766, -0.262342],
 [1.83072, -0.262342],
 [0.261532, -0.787027],
 [0.784595, -0.787027],
 [1.30766, -0.787027],
 [1.83072, -0.787027],
 [0.261532, -1.31171],
 [0.784595, -1.31171],
 [1.30766, -1.31171],
 [1.83072, -1.31171],
 [0.261532, -1.8364],
 [0.784595, -1.8364],
 [1.30766, -1.8364],
 [1.83072, -1.8364],
 [0.261532, -2.36108],
 [0.784595, -2.36108],
 [1.30766, -2.36108],
 [1.83072, -2.36108],
 [0.261532, -2.88577],
 [0.784595, -2.88577],
 [1.30766, -2.88577],
 [1.83072, -2.88577],
 [0.261532, -3.41045],
 [0.784595, -3.41045],
 [1.30766, -3.41045],
 [1.83072, -3.41045],
 [0.261532, -3.93513],
 [0.784595, -3.93513],
 [1.30766, -3.93513],
 [1.83072, -3.93513]])

box_height = (pl[-1][0] - pl[0][0]) / (4-1)
box_width = -(pl[-1][1] - pl[0][1]) / (8-1)

ap = {'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
      'r16', 'r17', 'r18', 'r19', 'r20', 'r21', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30', 'r31',
      'r', 'b'}

regions = {
    (0, 0, 1): set(['r0', 'r']),
    (0, 1, 1): set(['r1', 'r']),
    (0, 2, 1): set(['r2', 'r']),
    (0, 3, 1): set(['r3', 'r']),
    (1, 0, 1): set(['r4', 'r']),
    (1, 1, 1): set(['r5', 'r']),
    (1, 2, 1): set(['r6', 'r']),
    (1, 3, 1): set(['r7', 'r']),
    (2, 0, 1): set(['r8', 'r']),
    (2, 1, 1): set(['r9', 'r']),
    (2, 2, 1): set(['r10', 'r']),
    (2, 3, 1): set(['r11', 'r']),
    (3, 0, 1): set(['r12', 'r']),
    (3, 1, 1): set(['r13', 'r']),
    (3, 2, 1): set(['r14', 'r']),
    (3, 3, 1): set(['r15', 'r']),
    (4, 0, 1): set(['r16', 'r']),
    (4, 1, 1): set(['r17', 'r']),
    (4, 2, 1): set(['r18', 'r']),
    (4, 3, 1): set(['r19', 'r']),
    (5, 0, 1): set(['r20', 'r']),
    (5, 1, 1): set(['r21', 'b']),
    (5, 2, 1): set(['r22', 'r']),
    (5, 3, 1): set(['r23', 'r']),
    (6, 0, 1): set(['r24', 'r']),
    (6, 1, 1): set(['r25', 'r']),
    (6, 2, 1): set(['r26', 'r']),
    (6, 3, 1): set(['r27', 'r']),
    (7, 0, 1): set(['r28', 'r']),
    (7, 1, 1): set(['r29', 'r']),
    (7, 2, 1): set(['r30', 'r']),
    (7, 3, 1): set(['r31', 'r'])
}

edges = [
    ((0, 0, 1), (1, 0, 1)),
    ((1, 0, 1), (2, 0, 1)),
    ((2, 0, 1), (3, 0, 1)),
    ((3, 0, 1), (4, 0, 1)),
    ((4, 0, 1), (5, 0, 1)),
    ((5, 0, 1), (6, 0, 1)),
    ((6, 0, 1), (7, 0, 1)),
    ((0, 1, 1), (1, 1, 1)),
    ((1, 1, 1), (2, 1, 1)),
    ((2, 1, 1), (3, 1, 1)),
    ((3, 1, 1), (4, 1, 1)),
    ((4, 1, 1), (5, 1, 1)),
    ((5, 1, 1), (6, 1, 1)),
    ((6, 1, 1), (7, 1, 1)),
    ((0, 2, 1), (1, 2, 1)),
    ((1, 2, 1), (2, 2, 1)),
    ((2, 2, 1), (3, 2, 1)),
    ((3, 2, 1), (4, 2, 1)),
    ((4, 2, 1), (5, 2, 1)),
    ((5, 2, 1), (6, 2, 1)),
    ((6, 2, 1), (7, 2, 1)),
    ((0, 3, 1), (1, 3, 1)),
    ((1, 3, 1), (2, 3, 1)),
    ((2, 3, 1), (3, 3, 1)),
    ((3, 3, 1), (4, 3, 1)),
    ((4, 3, 1), (5, 3, 1)),
    ((5, 3, 1), (6, 3, 1)),
    ((6, 3, 1), (7, 3, 1)),
    ((0, 0, 1), (0, 1, 1)),
    ((0, 1, 1), (0, 2, 1)),
    ((0, 2, 1), (0, 3, 1)),
    ((1, 0, 1), (1, 1, 1)),
    ((1, 1, 1), (1, 2, 1)),
    ((1, 2, 1), (1, 3, 1)),
    ((2, 0, 1), (2, 1, 1)),
    ((2, 1, 1), (2, 2, 1)),
    ((2, 2, 1), (2, 3, 1)),
    ((3, 0, 1), (3, 1, 1)),
    ((3, 1, 1), (3, 2, 1)),
    ((3, 2, 1), (3, 3, 1)),
    ((4, 0, 1), (4, 1, 1)),
    ((4, 1, 1), (4, 2, 1)),
    ((4, 2, 1), (4, 3, 1)),
    ((5, 0, 1), (5, 1, 1)),
    ((5, 1, 1), (5, 2, 1)),
    ((5, 2, 1), (5, 3, 1)),
    ((6, 0, 1), (6, 1, 1)),
    ((6, 1, 1), (6, 2, 1)),
    ((6, 2, 1), (6, 3, 1)),
    ((7, 0, 1), (7, 1, 1)),
    ((7, 1, 1), (7, 2, 1)),
    ((7, 2, 1), (7, 3, 1))
]


def calc_box_id(x, y):
    # diff = np.abs(np.array([x, y]) - np.array(pl[0, :]))
    # return np.round(diff[1] / box_width) * 4 + (np.round(diff[0] / box_height) + 1)

    norm = np.linalg.norm(pl - np.array([x, y]), axis=1)

    # This is from 0 to 31. Real box id is norm + 1
    return np.argmin(norm)