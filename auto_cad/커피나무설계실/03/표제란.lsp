; ������� 
; ���� �պκ��� [ ; ] ǥ�ô� ���α׷��� �ڵ�� ���࿡�� ������ ���� �ʴ� �ּ��� �Դϴ�.
; �����е��� ; ǥ�ø� ����������� �Ʒ� �ҽ��ڵ�ó�� ���� ����ϼ���
; ��)
;(defun c:msh()   (command "change" pause "" "" "" "STANDARD" "" "" "SHAFT"))
;(defun c:�����ɾ�()   (command "change" pause "" "" "" "STANDARD" "" "" "ǥ���� �ܾ ���� �Է�"))

;===============================================================
; [1. ǰ���]

(defun c:msh()   (command "change" pause "" "" "" "STANDARD" "" "" "SHAFT"))
(defun c:mpl()   (command "change" pause "" "" "" "STANDARD" "" "" "PLATE"))
(defun c:mbr()   (command "change" pause "" "" "" "STANDARD" "" "" "BRK'T"))
(defun c:mbl()   (command "change" pause "" "" "" "STANDARD" "" "" "BLOCK"))
(defun c:mmp()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G PLATE"))
(defun c:mmbr()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G BRK'T"))
(defun c:mmt()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G"))
(defun c:mgu()   (command "change" pause "" "" "" "STANDARD" "" "" "GUIDE"))

;===============================================================
; [2. �����]

(defun c:m41()   (command "change" pause "" "" "" "STANDARD" "" "" "SS41"))
(defun c:m45()   (command "change" pause "" "" "" "STANDARD" "" "" "S45C"))
(defun c:msu()   (command "change" pause "" "" "" "STANDARD" "" "" "SUS304"))

(defun c:SK()   (command "change" pause "" "" "" "STANDARD" "" "" "SKD11"))
(defun c:SU()  M45 (command "change" pause "" "" "" "STANDARD" "" "" "SUJ2"))

(defun c:HG()   (command "change" pause "" "" "" "STANDARD" "" "" "������"))
(defun c:AL()   (command "change" pause "" "" "" "STANDARD" "" "" "AL6061"))
DK(defun c:AT()   (command "change" pause "" "" "" "STANDARD" "" "" "���� ��ũ��"))
(defun c:PC()   (command "change" pause "" "" "" "STANDARD" "" "" "PC(����)"))
(defun c:mal()   (command "change" pause "" "" "" "STANDARD" "" "" "AL6061"))
(defun c:mpc()   (command "change" pause "" "" "" "STANDARD" "" "" "����PC"))
(defun c:mdg()   (command "change" pause "" "" "" "STANDARD" "" "" "���ݺ�"))
(defun c:MC()   (command "change" pause "" "" "" "STANDARD" "" "" "MC NYLON (BLACK)"))

;===============================================================
; [3. ��ó��, ��ó����]

(defun c:HRC()  (command "change" pause "" "" "" "STANDARD" "" "" "05. ��ü��ó�� HRC45�̻�"))
(defun c:HR()   (command "change" pause "" "" "" "STANDARD" "" "" "Cr����,��ó��"))
(defun c:CR()   (command "change" pause "" "" "" "STANDARD" "" "" "Cr����"))
(defun c:BB()   (command "change" pause "" "" "" "STANDARD" "" "" "����Ƴ����¡"))
(defun c:HH()   (command "change" pause "" "" "" "STANDARD" "" "" "�ϵ�Ƴ����¡"))

(defun c:mcr()   (command "change" pause "" "" "" "STANDARD" "" "" "ũ�ҵ���"))
(defun c:mjh()   (command "change" pause "" "" "" "STANDARD" "" "" "���ؿ���"))
(defun c:mis()   (command "change" pause "" "" "" "STANDARD" "" "" "�λ꿰"))
(defun c:mish()   (command "change" pause "" "" "" "STANDARD" "" "" "�λ꿰(������)"))
(defun c:mdm()   (command "change" pause "" "" "" "STANDARD" "" "" "�ܸ�������"))bb 
(defun c:mym()   (command "change" pause "" "" "" "STANDARD" "" "" "���������"))
(defun c:mjj()   (command "change" pause "" "" "" "STANDARD" "" "" "�����Ǹ�"))
(defun c:jjg()   (command "change" pause "" "" "" "STANDARD" "" "" "�����Ǹ�(�����)"))
(defun c:myj()   (command "change" pause "" "" "" "STANDARD" "" "" "�����Ǹ�"))

(defun c:NA()   (command "change" pause "" "" "" "STANDARD" "" "" "ȫ�浿"))
(defun c:MI1()  (command "change" pause "" "" "" "STANDARD" "" "" "��2EA�� ��1EA�� ��Ī�����Ұ�."))
(defun c:MI2() (command "change" pause "" "" "" "STANDARD" "" "" "��4EA�� ��2EA�� ��Ī�����Ұ�."))
(defun c:MI3() (command "change" pause "" "" "" "STANDARD" "" "" "��6EA�� ��3EA�� ��Ī�����Ұ�."))
(defun c:MI4() (command "change" pause "" "" "" "STANDARD" "" "" "��8EA�� ��4EA�� ��Ī�����Ұ�."))



