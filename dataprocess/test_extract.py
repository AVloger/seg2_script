import numpy as np
import cv2
import pickle
import matplotlib.pyplot as plt

def draw_skeleton_rgb(img,valid_nodes):
    #构建骨骼
    _edges = [(9, 2), (2, 1), (1, 16), (1, 17), (16, 18), (17, 19), (2, 3), (2, 6),
                    (3, 4), (4, 5), (6, 7), (7, 8), (9, 10), (10, 11),
                    (11, 12), (12, 25), (12, 23), (23, 24), (9, 13), (13, 14),
                    (14, 15), (15, 22), (15, 20), (20, 21)]
    edges = []
    for edge in _edges:
        edges.append((edge[0]-1,edge[1]-1))
    # 画出有效的骨骼点
#         print(self.valid_nodes.shape)
    draw_nodes = valid_nodes.copy()
    # draw_nodes[:,0] = 1280 - draw_nodes[:,0]
    # draw_nodes[:,1] = 720 - draw_nodes[:,1]

    point_size = 2
    thickness = 10
    point_color = (255,0,0) # BGR
    draw_nodes = draw_nodes.astype(int)
    # 画出骨骼边
    _color = (0,0,255)
    node_indice = valid_nodes.copy()[:,:2]
    indices = valid_nodes[:, 0] == 0
    indices = indices == False
    for edge in edges:
        if indices[edge[0]] and indices[edge[1]]:
            p1 = node_indice[edge[0],:].astype(int)
            p2 = node_indice[edge[1],:].astype(int)
            cv2.line(img,tuple(p1),tuple(p2),_color,thickness=10)
    for node in draw_nodes:
        cv2.circle(img, tuple(node[:2]), point_size, point_color, thickness)
    return img
def get_img(video_name,frame=0):
    cap = cv2.VideoCapture(video_name)
    cap.set(cv2.CAP_PROP_POS_FRAMES,frame)  #设置要获取的帧号
    ret,img=cap.read()  #read方法返回一个布尔值和一个视频帧。若帧读取成功，则返回True
    if ret is False:
        #若读取该帧失败，则默认读取第0帧
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        ret,img=cap.read()
    return img
if __name__ == '__main__':
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter("result2.avi", fourcc, 20.0, (1280, 720), True)
    node_path = 'n38_p01.npy'
    nodes = np.load(node_path)
    video_path = 'p01_2.mp4'

    for frame_id in range(nodes.shape[0]):
        img = get_img(video_path,frame_id)
        node = nodes[frame_id]
        img = draw_skeleton_rgb(img,node)
        writer.write(img)
        cv2.imshow("test", img)
        key = cv2.waitKey(1)
        #     time.sleep(0.05)
        if key == ord('q'):
            break
        elif key == ord(' '):
            key = None
            while key != ord(' '):
                key = cv2.waitKey(1)
    writer.release()
    cv2.destroyAllWindows()