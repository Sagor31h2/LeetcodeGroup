package main

import "fmt"

type Node struct {
	val  int
	next *Node
}

// type LinkedList struct{
// 	head *Node
// }

func (li *Node) insert(key int) {
	nd := &Node{
		val:  key,
		next: nil,
	}
	flg := 0
	if li == nil {
		li = nd
		// fmt.Println("worked")
		flg = 1

	}

	temp := li
	for temp.next != nil {
		temp = temp.next
	}
	if flg == 0 {
		temp.next = nd
	}

	// if li == nil {
	// 	fmt.Println("list is empty")
	// 	return
	// }
	// temp = li
	// for temp != nil {
	// 	fmt.Println(temp.val)
	// 	temp = temp.next
	// }

}

func (li *Node) print() {
	if li == nil {
		fmt.Println("list is empty")
		return
	}
	temp := li
	for temp != nil {
		fmt.Println(temp.val)
		temp = temp.next
	}
}

func main() {
	// li := &LinkedList{
	// 	head: nil,
	// }
	// var list_head *Node = &Node{
	// 	val:  10,
	// 	next: nil,
	// }
	// var list_head Node = Node{
	// 	val:  0,
	// 	next: nil,
	// }
	var list_head Node = nil
	list_head.insert(5)
	fmt.Print(list_head)
	list_head.insert(6)
	// list_head.insert(6)

	list_head.print()

}
