"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Vineet Burugu and Aarnav Chitari, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: vsb433
UT EID 2: ac84787
"""

import sys


class HeapError(Exception):
    """
    Custom exception class for heap errors.
    """


class BinaryHeap:
    """A modified binary heap implementation from the readings."""

    def __init__(self):
        """
        Initializes an empty binary heap.
        """
        self.__heap = []


    def _perc_up(self, i):
        """
        Moves the element at index i up to its correct position in the heap.
        """
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self.__heap[i] < self.__heap[parent_idx]:
                self.__heap[i], self.__heap[parent_idx] = (
                    self.__heap[parent_idx],
                    self.__heap[i],
                )
            i = parent_idx


    def insert(self, item):
        """
        Inserts a new item into the heap and maintains the heap property.
        """
        self.__heap.append(item)
        self._perc_up(len(self.__heap) - 1)


    def _perc_down(self, i):
        """
        Moves the element at index i down to its correct position in the heap."""
        while 2 * i + 1 < len(self.__heap):
            sm_child = self._get_min_child(i)
            if self.__heap[i] > self.__heap[sm_child]:
                self.__heap[i], self.__heap[sm_child] = (
                    self.__heap[sm_child],
                    self.__heap[i],
                )
            else:
                break
            i = sm_child


    def _get_min_child(self, i):
        """
        Returns the index of the smaller child of the node at index i.
        """
        if 2 * i + 2 > len(self.__heap) - 1:
            return 2 * i + 1
        if self.__heap[2 * i + 1] < self.__heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2


    def delete(self):
        """
        Removes and returns the smallest item from the heap."""
        if self.is_empty():
            raise HeapError("Heap is empty")
        self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]
        result = self.__heap.pop()
        self._perc_down(0)
        return result


    def peek(self):
        """
        Returns the smallest item from the heap without removing it.
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.__heap[0]


    def is_empty(self):
        """
        Checks if the heap is empty."""
        return len(self.__heap) == 0


    def heapify(self, not_a_heap):
        """
        Converts a list into a heap in O(n) time."""
        self.__heap = not_a_heap[:]
        i = len(self.__heap) // 2 - 1
        while i >= 0:
            self._perc_down(i)
            i = i - 1


class Node:
    """
    Represents a node in a singly linked list.

    Instance Variables:
        data: The value or data stored in the node.
        next: The reference to the next node in the linked list (None by default).
    """

    def __init__(self, data, link=None):
        """
        Initializes a new node with the given data and a reference to the next node.

        Args:
            data: The data to store in the node.
            next: Optional; the next node in the linked list (None by default).
        """
        self.data = data
        self.next = link


    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next


    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")


class StackError(Exception):
    """
    Custom exception class for stack errors.
    """


class Stack:
    """
    A class that implements a stack using a singly linked list.

    Instance Variables:
        _top: The top node of the stack.
        _size: The number of elements in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack with no elements.
        """
        self._top = None
        self._size = 0


    def peek(self):
        """
        Returns the value at the top of the stack without removing it.

        Raises:
            StackError: If the stack is empty, raises "Peek from empty stack.".

        Returns:
            The data stored in the top node of the stack.
        """
        if self.is_empty():
            raise StackError("Peek from empty stack.")
        return self._top.data


    def push(self, item):
        """
        Pushes a new item onto the top of the stack.

        Args:
            item: The data to push onto the stack.
        """
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1


    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Raises:
            StackError: If the stack is empty, raises "Pop from empty stack.".

        Returns:
            The data from the top node of the stack.
        """
        if self.is_empty():
            raise StackError("Pop from empty stack.")
        removed_data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return removed_data


    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self._top is None


    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            The size of the stack as an integer.
        """
        return self._size


class Vertex:
    """Vertex Class using properties and setters for better encapsulation."""

    def __init__(self, label):
        self.__label = label
        self.visited = False
        self.depth = -1


    @property
    def visited(self):
        """Property to get the visited status of the vertex."""
        return self.__visited


    @visited.setter
    def visited(self, value):
        """Setter to set the visited status of the vertex."""
        if isinstance(value, bool):
            self.__visited = value
        else:
            raise ValueError("Visited status must be a boolean value.")


    @property
    def depth(self):
        """Property to get the depth of the vertex. This is the number of prereqs
        that need to be completed before this course."""
        return self.__depth


    @depth.setter
    def depth(self, value):
        """Setter to set the visited status of the vertex."""
        if isinstance(value, int):
            self.__depth = value
        else:
            raise ValueError("Depth must be a integer value.")


    @property
    def label(self):
        """Property to get the label of the vertex."""
        return self.__label


    def __str__(self):
        """String representation of the vertex"""
        return str(self.__label)


class Graph:
    """A Class to present a Graph."""

    def __init__(self):
        self.vertices = []  # a list of vertex objects
        self.adjacency_matrix = []  # adjacency matrix of edges


    def has_vertex(self, label):
        """Check if a vertex is already in the graph"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return True
        return False


    def get_index(self, label):
        """Given a label get the index of a vertex"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return i
        return -1


    def add_vertex(self, label):
        """Add a Vertex with a given label to the graph"""
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            self.adjacency_matrix[i].append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(num_vertices):
            new_row.append(0)
        self.adjacency_matrix.append(new_row)


    def add_edge(self, start, finish):
        """Add unweighted directed edge to graph"""
        self.adjacency_matrix[start][finish] = 1


    def get_adjacent_vertices(self, vertex_index):
        """Return adjacent vertex indices to vertex_index"""
        vertices = []
        num_vertices = len(self.vertices)
        for j in range(num_vertices):
            if self.adjacency_matrix[vertex_index][j]:
                vertices.append(j)
        return vertices


    def compute_depth(self):
        """Computes depth for each vertex in the graph."""
        h = [[] for _ in range(len(self.vertices))]
        k = [0 for _ in range(len(self.vertices))]
        for u in range(len(self.vertices)):
            for v in self.get_adjacent_vertices(u):
                h[v].append(u)
                k[u] = k[u] + 1
        queue = []
        for i, z in enumerate(k):
            if z == 0:
                queue.append(i)
                self.vertices[i].depth = 0
        while queue:
            u = queue.pop(0)
            for v in h[u]:
                self.vertices[v].depth = max(self.vertices[v].depth, self.vertices[u].depth + 1)
                k[v] = k[v] - 1
                if k[v] == 0:
                    queue.append(v)

    def has_cycle(self):
        """
        Determine whether or not the graph has a cycle.

        post: returns True if there is a cycle and False otherwise.
        """
        a = []
        for _ in range(len(self.vertices)):
            a.append(False)
        b = []
        for _ in range(len(self.vertices)):
            b.append(False)
        def z(v):
            a[v] = True
            b[v] = True
            for n in self.get_adjacent_vertices(v):
                if not a[n]:
                    if z(n):
                        return True
                elif b[n]:
                    return True
            b[v] = False
            return False
        for i in range(len(self.vertices)):
            if not a[i]:
                if z(i):
                    return True
        return False


    def get_registration_plan(self):
        """
        Return a valid ordering of courses to take for registration as a 2D
        list of vertex labels, where each inner list will have a maximum of 4 vertices.

        pre: a valid registration plan exists.
        post: returns a 2D list of strings, where each inner list represents a semester
        """
        courses = []
        n = len(self.vertices)
        indeg = [0] * n

        for u in range(n):
            for v in range(n):
                if self.adjacency_matrix[u][v] == 1:
                    indeg[v] += 1

        aval = []

        for i in range(n):
            if indeg[i] == 0:
                aval.append(i)

        while aval:
            aval.sort(key=lambda x:(-self.vertices[x].depth, self.vertices[x].label))

            sem = []
            aval2 = []

            for _ in range(min(4, len(aval))):
                u = aval.pop(0)
                sem.append(self.vertices[u].label)

                for v in self.get_adjacent_vertices(u):
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        aval2.append(v)

            courses.append(sem)
            aval.extend(aval2)

        return courses


def main():
    """
    The main function to retrieve a registration plan.
    The output code has been written for you.
    """

    # create a Graph object
    graph = Graph()

    # read the number of vertices
    verticies_count = int(sys.stdin.readline())

    # read the vertices and add them into the graph
    for _ in range(verticies_count):
        label = sys.stdin.readline().strip()
        graph.add_vertex(label)
    # read the number of edges
    edgescount = int(sys.stdin.readline())
    # read the edges and insert them into the graph
    for _ in range(edgescount):
        line = sys.stdin.readline().strip()
        if line == "":
            continue
        startlabel, endlabel = line.split()
        startidx = graph.get_index(startlabel)
        endidx = graph.get_index(endlabel)
        graph.add_edge(startidx, endidx)
    # you will need to call the method to convert them from their labels to their index

    ####################################################################################
    # DO NOT CHANGE ANYTHING BELOW THIS
    if graph.has_cycle():
        print("Registration plan invalid because a cycle was detected.")
    else:
        print("Valid registration plan detected.")
        graph.compute_depth()

        courses = graph.get_registration_plan()
        print()
        print("Registration plan: ")
        for semester in courses:
            print(semester)


if __name__ == "__main__":
    main()
