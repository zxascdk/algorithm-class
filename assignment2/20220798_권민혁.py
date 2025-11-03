class Node: # 단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, next=None): 
        self.data = elem
        self.link = next
    
    def append(self, new): # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new
    
    def popNext(self): # 현재 노드의 다음 노드를 삭제한 후 반환
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node
    
class LinkedList: # 단순 연결 리스트 크래스
    def __init__(self):
        self.head = None
    
    def isEmpty(self): # 리스트가 비어있는지 검사
        return self.head is None
    
    def insert(self, pos, elem): # pos 위치에 노드 추가
        if pos < 0:
            return
        
        new_node = Node(elem)
        before = self.getNode(pos - 1)
        
        if before is None:
            if pos == 0: 
                new_node.link = self.head
                self.head = new_node
            else:  
                raise IndexError("오류 : 리스트 범위를 벗어났습니다.")
        else:  
            before.append(new_node)
    
    def delete(self, pos): # pos 위치의 노드 삭제
        if pos < 0:
            return
        
        if pos == 0: 
            if self.head is None:
                raise IndexError("오류 : 빈 리스트에서 삭제할 수 없습니다.")
            self.head = self.head.link
        else: 
            before = self.getNode(pos - 1)
            if before is None:
                raise IndexError("오류 : 리스트 범위를 벗어났습니다.")
            if before.link is None:
                raise IndexError("오류 : 삭제할 노드가 없습니다.")
            before.popNext()
    
    def getNode(self, pos): # pos 위치의 노드 반환
        if pos < 0:
            return None
        
        if self.head is None:
            return None
        
        node = self.head
        for _ in range(pos):
            if node is None:  
                return None
            node = node.link
        
        return node
    
    def getEntry(self, pos): # pos 위치의 노드 데이터 반환
        node = self.getNode(pos)
        if node is None:
            return None
        return node.data
    
    def size(self): # 리스트 크기 반환
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.link
        return count
    
    def find_by_title(self, title): # 책 제목으로 도서 찾기
        node = self.head
        while node is not None:
            if node.data.title == title:
                return node.data
            node = node.link
        return None
    
    def find_pos_by_title(self, title): # 책 제목으로 도서 위치 찾기
        node = self.head
        pos = 0
        while node is not None:
            if node.data.title == title:
                return pos
            node = node.link
            pos += 1
        return -1
    
class Book: # 도서 정보 저장 클래스
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    
    def display(self): # 도서 정보 출력
        print(f"[책 번호: {self.book_id}, 책 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]")


class BookManagement: # 도서 관리 프로그램 클래스
    def __init__(self):
        self.book_list = LinkedList()
    
    def add_book(self, book_id, title, author, year): # 도서 추가
        node = self.book_list.head
        while node is not None:
            if node.data.book_id == book_id:
                print(f"오류 : 책 번호 {book_id}는 이미 존재합니다.")
                return
            node = node.link
        
        new_book = Book(book_id, title, author, year)
        self.book_list.insert(self.book_list.size(), new_book)
        print(f"도서 '{title}'가 추가되었습니다.")
    
    def remove_book(self, title): # 도서 삭제
        pos = self.book_list.find_pos_by_title(title)
        if pos == -1:
            print(f"오류 : 도서 '{title}'를 찾을 수 없습니다.")
        else:
            self.book_list.delete(pos)
            print(f"도서 '{title}'가 삭제되었습니다.")
    
    def search_book(self, title): # 도서 조회(검색)
        book = self.book_list.find_by_title(title)
        if book is None:
            print(f"오류 : 도서 '{title}'를 찾을 수 없습니다.")
        else:
            print("\n=== 도서 조회 결과 ===")
            book.display()
    
    def display_books(self): # 등록된 모든 도서 출력
        if self.book_list.isEmpty():
            print("현재 등록된 도서가 없습니다.")
        else:
            print("\n현재 등록된 도서 목록 : ")
            node = self.book_list.head
            while node is not None:
                node.data.display()
                node = node.link
    
    def run(self): # 프로그램 실행
        while True:
            print("\n==============================")
            print("=== 도서 관리 프로그램 ===")
            print("==============================")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            print("==============================")
            
            try:
                choice = input("메뉴를 선택하세요 : ")
                
                if choice == '1':
                    print("\n===== 도서 추가 =====")
                    book_id = input("책 번호를 입력하세요 : ")
                    title = input("책 제목을 입력하세요 : ")
                    author = input("저자를 입력하세요 : ")
                    year = input("출판 연도를 입력하세요 : ")
                    self.add_book(book_id, title, author, year)
                
                elif choice == '2':
                    print("\n===== 도서 삭제 =====")
                    title = input("삭제할 책 제목을 입력하세요 : ")
                    self.remove_book(title)
                
                elif choice == '3':
                    print("\n===== 도서 조회 =====")
                    title = input("조회할 책 제목을 입력하세요 : ")
                    self.search_book(title)
                
                elif choice == '4':
                    self.display_books()
                
                elif choice == '5':
                    print("\n도서 관리 프로그램을 종료합니다.")
                    break
                
                else:
                    print("잘못된 메뉴 선택입니다. 1~5 사이의 숫자를 입력하세요.")
            
            except KeyboardInterrupt:
                print("\n\n도서 관리 프로그램을 종료합니다.")
                break
            except Exception as e:
                print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    management = BookManagement()
    management.run()


