#!/usr/bin/python
from ImportClinicOdontomed.import_tb_om_profissionais import executa_import_profissionais

# Variáveis Globais


''' Layout do Arquivo:
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ======= ========== =============== ===============  
|  1  |       2      |    3     |          4          |   5      |      6     |      7     | 8 |    9    |   10  |  11   |    12    |      13       |       14
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ======= ========== =============== ===============
|DATA | PROFISSIONAL | PACIENTE | CONVENIO/PARTICULAR |  D/C     | TP CRÉDITO | N PARCELAS | % | ENTRADA | SAIDA | SALDO | DESCONTO | TOTAL LIQUIDO | Campo Controle
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ================== =============== =============== 
                                    particular          débito      a vista                        > 0      < 0                                         0: ?
                                    odontoprev          crédito     a prazo                                                                             1: Pulo Linha
                                    bradesco                                                                                                            2: Profissional   
                                    interodonto
====================================================================================================================================================                                    
'''
if __name__ == '__main__':
    executa_import_profissionais()

