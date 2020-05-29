from hamcrest import *
from bin_tree import Tree, max_distance, max_distance_tree

def test_single_node():
    t = Tree()
    assert_that(max_distance(t), equal_to(0))

def test_two_nodes_left():
    t = Tree()
    t.left = Tree()
    assert_that(max_distance(t), equal_to(1))    

def test_two_nodes_right():
    t = Tree()
    t.right = Tree()
    assert_that(max_distance(t), equal_to(1))    

def test_three_nodes():
    t = Tree()
    t.right = Tree()
    t.left = Tree()
    assert_that(max_distance(t), equal_to(2))    

def test_four_nodes():
    t = Tree()
    t.right = Tree()
    t.right.right = Tree()
    t.left = Tree()
    assert_that(max_distance(t), equal_to(3))    

def test_four_nodes_unbalanced():
    t = Tree()
    t.right = Tree()
    t.right.right = Tree()
    t.right.left = Tree()
    assert_that(max_distance(t), equal_to(2))    

def test_four_nodes_unbalanced_spread():
    t = Tree()
    t.right = Tree()
    t.right.right = Tree()
    t.left = Tree()
    assert_that(max_distance(t), equal_to(3))    


def test_five_nodes():
    t = Tree()
    t.right = Tree()
    t.right.right = Tree()
    t.left = Tree()
    t.left.left = Tree()
    assert_that(max_distance(t), equal_to(4))    


def test_eight_nodes_unbalanced():
    t = Tree()
    t.right = Tree()

    t.right.left = Tree()
    t.right.left.left = Tree()
    t.right.left.left.left = Tree()


    t.right.right = Tree()
    t.right.right.right = Tree()
    t.right.right.right.right = Tree()

    assert_that(max_distance(t), equal_to(6))

def test_height_single_node():
    t = Tree()
    assert_that(max_distance_tree(t)[1], equal_to(0))

def test_height_two_nodes_left():
    t = Tree()
    t.left = Tree()
    assert_that(max_distance_tree(t)[1], equal_to(1))    

def test_height_two_nodes_right():
    t = Tree()
    t.right = Tree()
    assert_that(max_distance_tree(t)[1], equal_to(1))    

def test_height_three_nodes_unbalanced():
    t = Tree()
    t.left = Tree()
    t.left.left = Tree()
    assert_that(max_distance_tree(t)[1], equal_to(2))    
