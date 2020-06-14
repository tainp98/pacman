from collections import defaultdict 
from pygame.math import Vector2 as vec
from settings import *
class BFS: 
    def __init__(self, app): 
        self.app = app
        self.graph = defaultdict(list) 
        self.parent = dict()
        self.nodes_across = 0
        for node in self.app.empty_coins:
            node = self.get_pix_pos(node)
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

                # Get node position
                #pos_current_node = App.pacman.get_pix_pos(current_node.position)
                node_position = vec(node.x + new_position[0]*self.app.cell_width, node.y + new_position[1]*self.app.cell_height)

                # Make sure within range
                if node_position[0] > MAZE_WIDTH or node_position[0] < 0 or node_position[1] > MAZE_HEIGHT or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                break0 = False
                for wall in self.app.wall:
                    pix_wall = self.get_pix_pos(wall)
                    a = self.get_pix_pos(vec(1,1))
                    if node_position == pix_wall or node_position == a:
                        break0 = True
                        break
                if break0 == True: 
                    continue
                # Create new node
                self.graph[(node.x,node.y)].append(node_position) 
            
    def get_pix_pos(self,position):
        return vec(position.x*self.app.cell_width+self.app.cell_width//2,
                position.y*self.app.cell_height+self.app.cell_height//2)
    def BFS(self, start, end): 
        start = self.get_pix_pos(start)
        end = self.get_pix_pos(end)
        # Mark all the vertices as not visited 
        graph_keys = [vec(i[0],i[1]) for i in self.graph]
        visited = [False] * (len(graph_keys)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(start) 
        visited[graph_keys.index(start)] = True
        self.parent[(start.x,start.y)] = None
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            for i in self.graph[(s.x,s.y)]:
                if visited[graph_keys.index(i)] == False: 
                    queue.append(i) 
                    visited[graph_keys.index(i)] = True
                    self.nodes_across += 1
                    self.parent[(i.x,i.y)] = s
                    if i == end:
                        path = []
                        current = i
                        while current is not None:
                            path.append(current)
                            current = self.parent.get((current.x,current.y))
                        return path[::-1]
                
  
# Driver code 
  
# Create a graph given in 
# the above diagram 