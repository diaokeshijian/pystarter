#!/usr/bin/python
# -*- coding: utf-8 -*-


def test_list_split():
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print "before slice: "
    print nodes

    sliced_nodes = nodes[0:3]  # type: List[str]
    print "after slece:"
    print nodes
    print sliced_nodes


# test_list_split()


def test_string_split():
    str = "abcdef;"
    sub_str = str[: -1]
    print sub_str


# test_string_split()


def test_string_split_when_condition_not_match():
    str = 'CN=TAK1540T_2NB01'
    elements = str.split(',')
    for element in elements:
        print element


# test_string_split_when_condition_not_match()


def test_element_exists_in_list():
    some_element = 'ff'
    elements = ['ss', 'aa', 'ff', 'bb', 'ff']
    while some_element in elements:
        element_index = elements.index(some_element)
        print some_element, "'s index is: ", element_index
        elements.pop(element_index)
    for element in elements:
            index = elements.index(element)
            index = index + 1
            print "第", index, "个元素为: ", element


test_element_exists_in_list()
