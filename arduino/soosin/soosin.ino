#include <VirtualWire.h> // VirtualWire 라이브러리를 사용

const int rxPin = 2;    // 수신 핀, 디폴트: 11pin
const int ledPin = 10;  // LED용 핀 (내장)

void setup() {
        vw_setup(2000);       // 수신 속도
        vw_set_rx_pin(rxPin); // 수신 핀 설정
        vw_rx_start();        // 수신 시작

        pinMode(ledPin, OUTPUT);   // LED 핀 아웃풋으로 설정
        Serial.begin(9600);       // 시리얼 포트 9600으로 시작
        Serial.println("Ready!"); // 시리얼로 준비 출력
}

void loop() {

        uint8_t buff[VW_MAX_MESSAGE_LEN];     // 받은 메시지를 저장할 변수
        uint8_t buffLength = VW_MAX_MESSAGE_LEN; // 메시지의 크기

        if (vw_get_message(buff, &buffLength)) { // 메시지 수신 함수
              digitalWrite(ledPin, HIGH); // LED 켬
              for (int i = 0; i < buffLength; i++) { // 한 글자씩 출력
                   Serial.write(buff[i]); 
              }
              Serial.println(""); // 개행문자 출력]
              delay(500);
              digitalWrite(ledPin, LOW); // LED 끔
       }
}
