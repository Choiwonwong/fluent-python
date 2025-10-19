def process_command(command):
    match command:
        case ["add", *numbers]:
            # "add" 뒤에 오는 모든 항목을 numbers 리스트에 담습니다.
            total = sum(int(n) for n in numbers)
            print(f"합계: {total}")
            print(f"캡처된 변수(numbers): {numbers}, 타입: {type(numbers)}")
        case ["find", name]:
            print(f"{name}을(를) 찾습니다.")
        case _:
            print("알 수 없는 명령어입니다.")

# 테스트
process_command(["add", "10", "20", "30"])
# 출력:
# 합계: 60
# 캡처된 변수(numbers): ['10', '20', '30'], 타입: <class 'list'>

process_command(["add"]) # *numbers는 0개 항목도 매칭됩니다.
# 출력:
# 합계: 0
# 캡처된 변수(numbers): [], 타입: <class 'list'>

process_command(["find", "최원웅"])
# 출력:
# 최원웅을(를) 찾습니다.

print("=" * 20)
print("=" * 20)

def validate_packet(packet):
    match packet:
        case ["START", *_, "END"]:
            # "START"로 시작하고 "END"로 끝나면 중간에 몇 개가 있든 통과!
            # 중간 내용은 *_ 에 매칭되지만, 어떤 변수에도 저장되지 않습니다.
            print("✅ 유효한 패킷입니다.")
        case ["START", *_]:
            print("⚠️ 패킷이 'END'로 닫히지 않았습니다.")
        case [_, *_, "END"]:
             print("⚠️ 패킷이 'START'로 시작하지 않았습니다.")
        case _:
            print("❌ 잘못된 형식의 패킷입니다.")

# 테스트
validate_packet(["START", "data1", "data2", "data3", "END"])
# 출력: ✅ 유효한 패킷입니다.

validate_packet(["START", "END"]) # 중간에 0개 항목도 매칭됩니다.
# 출력: ✅ 유효한 패킷입니다.

validate_packet(["START", "data1", "data2"])
# 출력: ⚠️ 패킷이 'END'로 닫히지 않았습니다.

validate_packet(["junk", "data1", "END"])
# 출력: ⚠️ 패킷이 'START'로 시작하지 않았습니다.