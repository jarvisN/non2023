class Non:
    def __init__(self):
        # กำหนดค่าเริ่มต้นให้กับตัวแปร result เป็น None
        self.result = None

    def plus(self, num1, num2):
        # บวกเลข num1 และ num2 และเก็บผลลัพธ์ไว้ในตัวแปร result
        self.result = num1 + num2
        return self.result

    def __str__(self):
        # แสดงผลลัพธ์ในรูปแบบ "Result: {result}"
        return f"Result : {self.result}"
