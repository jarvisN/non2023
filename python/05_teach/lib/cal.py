class Non:
    def __init__(self):
        # กำหนดค่าเริ่มต้นให้กับตัวแปร result เป็น None
        self.result = None

    def plus(self, num1, num2):
        # บวกเลข num1 และ num2 และเก็บผลลัพธ์ไว้ในตัวแปร result
        self.result = num1 + num2
        
        # print("qwerty")
        return self.result

        # return "ok"
    def test(self):
        print(1234)
        return 5678

    def __str__(self):
        # แสดงผลลัพธ์ในรูปแบบ "Result: {result}"
        # return f"Result : {self.result}"
        # print('awer')
        # return "1234"
        pass
