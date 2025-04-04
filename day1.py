try:
    num1 = float(input("첫번째 숫자를 입력하세요:  "))
    num2 = float(input("두번째 숫자를 입력하세요: "))

    print("덧셈 결과:", num1 + num2)
    print("뺄셈 결과:", num1 - num2)
    print("곱셈 결과:", num1 * num2)

    if num2==0:
        print("0으로 나눌수 없습니다.")
        else:
    print("나눗셈 결과:", num1 / num2)

except ValueError:
    print("유효한 숫자를 입력하세요.")      

def find_min_max():
    """사용자로부터 리스트를 입력받아 최대값과 최소값을 출력합니다."""

    try:
        input_str= input("쉼표로 구분된 숫자들을 입력하세요 (예 : 1,5,3,7)")
        num_list = [float(num)for num in input_str.split(",")]
                    
        if not num_list:
           print("입력된 숫자가 없습니다.")
           return
       
        
        max_value = max(num_list)
        min_value = min(num_list)


        print("최대값:",max_value)
        print("최소값:",min_value)

    except ValueError:
        print("유효한 숫자가 아닙니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

find_min_max()  

def reverse_string():
    """사용자로부터 문자열을 입력받아 거꾸로 출력합니다."""

    input_str = input("문자열을 입력하세요:")
    reversed_str = input_str[::-1]
    print("거꾸로 출력: ", reversed_str)

reverse_string()  