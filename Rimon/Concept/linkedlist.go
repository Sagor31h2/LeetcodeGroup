package main

import "fmt"

type Node struct {
	data int
	next *Node
}
type LinkedList struct {
	head *Node
}

func (L *LinkedList) insert(key int) {
	nd := &Node{
		data: key,
		next: nil,
	}
	//when list is empty
	if L.head == nil {
		L.head = nd
		return
	}

	// temp := L.head
	// if temp == nil {		//does not work. dont know why
	// 	temp = nd
	// 	return
	// }

	var temp *Node = L.head
	for temp.next != nil {
		temp = temp.next
	}
	temp.next = nd
}

func (L *LinkedList) Print() {
	temp := L.head
	for temp != nil {
		fmt.Println(temp.data)
		temp = temp.next
	}
}

func main() {

	var list LinkedList = LinkedList{
		head: nil,
	}

	list.insert(1)
	list.insert(2)
	list.insert(3)
	list.insert(4)
	list.insert(5)
	list.insert(6)

	list.Print()

}
