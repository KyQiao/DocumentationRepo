def bfs(top_node, visit):
"""Breadth-first search on a graph, starting at top_node."""
	from collections import deque
	visited = set()
	queue = deque()
	queue.append(top_node)
	while len(queue):
		curr_node = queue.pop() # Dequeue
		visited.add(curr_node)
		visit(curr_node) # Visit the node
		# Enqueue non-visited and non-enqueued children
		queue.extend([c for c in curr_node.children
							if c not in visited or c not in queue])
# I think it should be fine to use the function