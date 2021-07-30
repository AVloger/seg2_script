import os
import numpy as np
import pandas as pd
from xlrd import open_workbook
import sys
def valid_action(action_type):

    if action_type == "2Axel_2AxelSEQ":
        action_type = "2Axel_2Axel_SEQ"
    if action_type == "2Axel_2Teoloop":
        action_type = "2Axel_2Toeloop"
    if action_type == "2Axel_3Teoloop":
        action_type = "2Axel_3Toeloop"
    if action_type == "2Axel_2Teoloop_2Loop":
        action_type = "2Axel_2Toeloop_2Loop"
    if action_type == "2Axel_2Teoloop_2Teoloop":
        action_type = "2Axel_2Toeloop_2Toeloop"
    if action_type == "2Axel_Eukar_3Salchow":
        action_type = "2Axel_Euler_3Salchow"
    if action_type == "2Lutz_2Teoloop_2Loop":
        action_type = "2Lutz_2Toeloop_2Loop"
    if action_type == "2Teoloop":
        action_type = "2Toeloop"
    if action_type == "3 Lutz_3Toeloop":
        action_type = "3Lutz_3Toeloop"
    if action_type == "3Axel_2Teoloop":
        action_type = "3Axel_2Toeloop"
    if action_type == "3Axel_3Teoloop":
        action_type = "3Axel_3Toeloop"
    if action_type == "3Filp":
        action_type = "3Flip"
    if action_type == "3Flip_2Teoloop":
        action_type = "3Flip_2Toeloop"
    if action_type == "3Flip_2Teoloop_2Loop":
        action_type = "3Flip_2Toeloop_2Loop"
    if action_type == "3Flip_3Teoloop":
        action_type = "3Flip_3Toeloop"
    if action_type == "3Loop_2Teoloop":
        action_type = "3Loop_2Toeloop"
    if action_type == "3Loop_3Teoloop":
        action_type = "3Loop_3Toeloop"
    if action_type == "3Lutz_2Teoloop":
        action_type = "3Lutz_2Toeloop"
    if action_type == "3Lutz_3Teoloop":
        action_type = "3Lutz_3Toeloop"
    if action_type == "3SalChow":
        action_type = "3Salchow"
    if action_type == "3Teoloop_2Teoloop":
        action_type = "3Toeloop_2Toeloop"
    if action_type == "3Teoloop_Euler_3Salchow":
        action_type = "3Toeloop_Euler_3Salchow"
    if action_type == "4Salchow_2Teoloop":
        action_type = "4Salchow_2Toeloop"
    if action_type == "4Salchow_3Teoloop":
        action_type = "4Salchow_3Toeloop"
    if action_type == "4Teoloop":
        action_type = "4Toeloop"
    if action_type == "4Teoloop_2Teoloop":
        action_type = "4Toeloop_2Toeloop"
    if action_type == "4Teoloop_3Axel_SEQ":
        action_type = "4Toeloop_3Axel_SEQ"
    if action_type == "4Teoloop_3Teoloop":
        action_type = "4Toeloop_3Toeloop"
    if action_type == "ChCombSpin4":
        action_type = "ChComboSpin4"
    if action_type == "ChCombeSpin4":
        action_type = "ChComboSpin4"
    if action_type == "ChComboSpin2V":
        action_type = "ChComboSpin2"
    if action_type == "ChComboSpin3 ":
        action_type = "ChComboSpin3"
    if action_type == "ChComboSpin3V":
        action_type = "ChComboSpin3"
    if action_type == "ChComboSpin4 ":
        action_type = "ChComboSpin4"
    if action_type == "ChSitSpin34":
        action_type = "ChSitSpin4"
    if action_type == "ChoreSequence1":
        action_type = "ChoreoSequence1"
    if action_type == "ChoreoSequance1":
        action_type = "ChoreoSequence1"
    if action_type == "ChoreoSequence":
        action_type = "ChoreoSequence1"
    if action_type == "ChroeoSequence1":
        action_type = "ChoreoSequence1"
    if action_type == "Fly itSpin4":
        action_type = "FlySitSpin4"
    if action_type == "FlyCamelSpin":
        action_type = "FlyCamelSpin1"
    if action_type == "FlyChComboSpin4V":
        action_type = "FlyChComboSpin4"
    if action_type == "LayBackSpin3":
        action_type = "LaybackSpin3"
    if action_type == "LayBackSpin4":
        action_type = "LaybackSpin4"
    if action_type == "StepSequece2":
        action_type = "StepSequence2"
    if action_type == "StepSequece3":
        action_type = "StepSequence3"
    if action_type == "StepSequnce3":
        action_type = "StepSequence3"
    if action_type == "StepSequnece2":
        action_type = "StepSequence2"
    if action_type == "StepSequnece3":
        action_type = "StepSequence3"
    if action_type == "3Teoloop":
        action_type = "3Toeloop"
    if action_type == "4Salohow_2Toeloop":
        action_type = "4Salchow_2Toeloop"
    if action_type == "3Axel_REP":
        action_type = "3Axel"
    if action_type == "3Flip_REP":
        action_type = "3Flip"
    if action_type == "4Toeloop_REP":
        action_type = "4Toeloop"
    if action_type == "3Salchow_REP":
        action_type = "3Salchow"
    if action_type == "3Lutz_COMBO":
        action_type = "3Lutz"
    if action_type == "3Lutz_REP":
        action_type = "3Lutz"
    if action_type == "4Lutz_REP":
        action_type = "4Lutz"
    if action_type == "3Flip_REP":
        action_type = "3Flip"
    if action_type == "4Salchow_REP":
        action_type = "4Salchow"
    if action_type == "3Flip_2Toeloop_2loop":
        action_type = "3Flip_2Toeloop_2Loop"
    if action_type == "4 Toeloop":
        action_type = "4Toeloop"
    if action_type == "Axel":
        action_type = "1Axel"
    if action_type == "3 Flip":
        action_type = "3Flip"
    if action_type == "Ch Sit Spin 4":
        action_type = "ChSitSpin4"
    if action_type == "Ch Camel Spin4":
        action_type = "ChCamelSpin4"
    if action_type == "Fly Sit Spin4":
        action_type = "FlySitSpin4"
    if action_type == "ChComolSpin2":
        action_type = "ChComolSpin2"
    if action_type == "CamelSpin":
        action_type = "CamelSpin1"
    if action_type == "2A_3T_2T":
        action_type = "2Axel_3Toeloop_2Toeloop"
    if action_type == "2A_3T_2T":
        action_type = "2Axel_3Toeloop_2Toeloop"
    if action_type == "4Filp":
        action_type = "4Flip"
    if action_type == "3S_2T_2Lo":
        action_type = "3Salchow_2Toeloop_2Loop"
    if action_type == "ChComboSpin1V":
        action_type = "ChComboSpin1"
    if action_type == "Fly Camel Spin 3":
        action_type = "FlyCamelSpin3"
    if action_type == "4 Toeloop_3 Toeloop":
        action_type = "4Toeloop_3Toeloop"
    if action_type == "ChComboSpin4V":
        action_type = "ChComboSpin4"
    if action_type == "3Lutz_3Toelloop":
        action_type = "3Lutz_3Toeloop"
    if action_type == "Step Sequence2":
        action_type = "StepSequence2"
    if action_type == "2A_1Eu_3S":
        action_type = "2Axel_1Euler_3Salchow"
    if action_type == "Fly Sit Spin3":
        action_type = "FlySitSpin3"
    if action_type == "FlySitSpin1V":
        action_type = "FlySitSpin1"
    if action_type == "4 Toeloop_2 Toeloop":
        action_type = "4Toeloop_2Toeloop"
    if action_type == "3F_2T_2T":
        action_type = "3Flip_2Toeloop_2Toeloop"
    if action_type == "Camel Spin":
        action_type = "CamelSpin1"
    if action_type == "Ch Combo Spin 4":
        action_type = "ChComboSpin4"
    if action_type == "ChComboSpin":
        action_type = "ChComboSpin1"
    if action_type == "FlySitSpin":
        action_type = "FlySitSpin1"
    if action_type == "StepSquence4":
        action_type = "StepSequence4"
    if action_type == "3A_2T_2T":
        action_type = "3Axel_2Toeloop_2Toeloop"
    if action_type == "3T_1Eu_2S":
        action_type = "3Toeloop_1Euler_2Salchow"
    if action_type == "2A+1Eu+3S":
        action_type = "2Axel_1Euler_3Salchow"
    if action_type == "3Flip*":
        action_type = "3Flip"
    if action_type == "LaybackSpin":
        action_type = "LaybackSpin1"
    if action_type == "ChCamelSpin":
        action_type = "ChCamelSpin1"
    if action_type == "StepSequence":
        action_type = "StepSequence1"
    if action_type == "FlyChComboSpin2V":
        action_type = "FlyChComboSpin2"
    if action_type == "FlyChComboSpin1V":
        action_type = "FlyChComboSpin1"
    if action_type == "StepSequence":
        action_type = "StepSequence1"

    if action_type == "2Lutz'":
        action_type = "2Lutz"
    if action_type == "4 Toeloop":
        action_type = "4Toeloop"
    if action_type == "Fly Camel Spin 4":
        action_type = "FlyCamelSpin 4"
    if action_type == "Ch Sit Spin 4":
        action_type = "ChSitSpin4"
    if action_type == "Step Sequence4":
        action_type = "StepSequence4"
    if action_type == "Ch combo Spin3":
        action_type = "ChComboSpin3"
    if action_type == "Ch Sit Spin4":
        action_type = "ChSitSpin4"
    if action_type == "Step Sequence3":
        action_type = "StepSequence3"
    if action_type == "Ch combo Spin4":
        action_type = "ChComboSpin4"
    if action_type == "Ch Combo Spin 4":
        action_type = "ChComboSpin4"
    if action_type == "4 Toeloop_3 Toeloop":
        action_type = "4Toeloop_3Toeloop"
    if action_type == "Fly Camel Spin 3":
        action_type = "FlyCamelSpin3"
    if action_type == "Step Sequence2":
        action_type = "StepSequence2"
    if action_type == "3 Flip":
        action_type = "3Flip"
    if action_type == "Fly Camel Spin 2":
        action_type = "FlyCamelSpin2"
    if action_type == "Fly Camel Spin 2":
        action_type = "FlyCamelSpin2"
    if action_type == "Ch Sit Spin":
        action_type = "ChSitSpin1"
    if action_type == "Ch Camel Spin3":
        action_type = "ChCamelSpin3"
    if action_type == "Fly Sit Spin3":
        action_type = "FlySitSpin3"
    if action_type == "Ch Camel Spin4":
        action_type = "ChCamelSpin4"
    if action_type == "Fly Sit Spin4":
        action_type = "FlySitSpin4"
    if action_type == "4 Toeloop_2 Toeloop":
        action_type = "4Toeloop_2Toeloop"
    if action_type == "3 Toeloop":
        action_type = "3Toeloop"
    if action_type == "Ch Combo Spin 3":
        action_type = "ChComboSpin3"
    if action_type == "3 Lutz":
        action_type = "3Lutz"
    if action_type == "4 Lutz":
        action_type = "4Lutz"
    if action_type == "Axel":
        action_type = "1Axel"
    if action_type == "ChComboSpin3V":
        action_type = "ChComboSpin3"
    if action_type == "ChComboSpin":
        action_type = "ChComboSpin1"
    if action_type == "ChComboSpin1V":
        action_type = "ChComboSpin1"
    if action_type == "ChComboSpin4V":
        action_type = "ChComboSpin4"

    if action_type == "1Axel<<":
        action_type = "1Axel"
    if action_type == "2Flip_Euler_2Salchow":
        action_type = "2Flip_1Euler_2Salchow"
    if action_type == "3Loop_Euler_3Salchow":
        action_type = "3Loop_1Euler_3Salchow"
    if action_type == "2Axel_Euler_1Flip":
        action_type = "2Axel_1Euler_1Flip"
    if action_type == "2Lutz_Euler_3Salchow":
        action_type = "2Lutz_1Euler_3Salchow"
    if action_type == "FlyiSitSpin3":
        action_type = "FlySitSpin3"
    if action_type == "FlySitSpin1V":
        action_type = "FlySitSpin1"
    if action_type == "ChComboSpin2V":
        action_type = "ChComboSpin2"
    if action_type == "FlySitSpin":
        action_type = "FlySitSpin1"
    if action_type == "CamelSpin":
        action_type = "CamelSpin1"
    if action_type == "CamelSpinB":
        action_type = "CamelSpin1"
    if action_type == "StepSequenceB":
        action_type = "StepSequence1"
    if action_type == "Salchow_Combo":
        action_type = "3Salchow_Combo"
    if action_type == "FlySitSpinB":
        action_type = "FlySitSpin1"
    if action_type == "3Salchow_2Axel_SEQ":
        action_type = "3Salchow_2Axel"
    if action_type == "FlyChSitSpin3":
        action_type = "FlyChSitSpin3"
    if action_type == "ChSitSpin":
        action_type = "ChSitSpin1"
    if action_type == "StepSequence":
        action_type = "StepSequence1"
    if action_type == "3Axel+REP":
        action_type = "3Axel_REP"
    if action_type == "Loop":
        action_type = "Loop1"
    if action_type == "ChCamelSpinB":
        action_type = "ChCamelSpin1"
    if action_type == "2Axel_Euler_2Toeloop":
        action_type = "2Axel_1Euler_2Toeloop"
    if action_type == "3Toeloop_2Axel_SEQ":
        action_type = "3Toeloop_2Axel"
    if action_type == "CSSp2V":
        action_type = "CSSp2"
    if action_type == "ChSitSpinB":
        action_type = "ChSitSpin1"
    if action_type == "CCSp1V":
        action_type = "CCSp1"
    if action_type == "3Toeloop+REP":
        action_type = "3Toeloop_REP"
    if action_type == "FlyChComboSpin2V":
        action_type = "FlyChComboSpin2"
    if action_type == "Camel Spin":
        action_type = "CamelSpin"
    if action_type == "Step_Sequence1":
        action_type = "StepSequence1"
    if action_type == "FLyChComboSpin2V":
        action_type = "FlyChComboSpin2"
    if action_type == "FLySitSpin2":
        action_type = "FlySitSpin2"
    if action_type == "FLySitSpin3":
        action_type = "FlySitSpin3"
    if action_type == "ChComboSpinB":
        action_type = "ChComboSpin1"
    if action_type == "StepSaquence":
        action_type = "StepSequence1"
    if action_type == "ChComolSpin43":
        action_type = "ChComolSpin4"
    if action_type == "2A_3T_2T":
        action_type = "2Axel_3Toeloop_2Toeloop"
    if action_type == "FlyChComboSpin":
        action_type = "FlyChComboSpin1"
    if action_type == "3T_1Eu_2S":
        action_type = "3Toeloop_1Euler_2Salchow"
    if action_type == "2A_1Eu_3S":
        action_type = "2Axel_1Euler_3Salchow"
    if action_type == "3Flip*":
        action_type = "3Flip"
    if action_type == "3F_2T_2T":
        action_type = "3Flip_2Toeloop_2Toeloop"
    if action_type == "3S_2T_2Lo":
        action_type = "3Salchow_2Toeloop_2Loop"
    if action_type == "2A+1Eu+3S":
        action_type = "2Axel_1Euler_3Salchow"
    if action_type == "3Salchow+3Loop":
        action_type = "3Salchow_3Loop"
    if action_type == "ChoreoSequence":
        action_type = "ChoreoSequence1"
    if action_type == "FlychCombo":
        action_type = "FlychComboSpin1"
    if action_type == "3Filp+3Toeloop":
        action_type = "3Filp_3Toeloop"
    if action_type == "StepSquence1":
        action_type = "StepSequence1"
    if action_type == "3Luta+3Toeloop":
        action_type = "3Lutz_3Toeloop"
    if action_type == "3Theloop_3Theloop":
        action_type = "3Toeloop_3Toeloop"
    if action_type == "FlyCamelSpin":
        action_type = "FlyCamelSpin1"
    if action_type == "StepSequenc2":
        action_type = "StepSequence2"
    if action_type == "StepSequenc":
        action_type = "StepSequence1"
    if action_type == "3Toeloop+3Toeloop":
        action_type = "3Toeloop_3Toeloop"
    if action_type == "3A_2T_2T":
        action_type = "3Axel_2Toeloop_2Toeloop"
    if action_type == "ChComboSpin3_n96_p12_g11":
        action_type = "ChComboSpin3"
    if action_type == "ChSitSpin3_n96_p12_g12":
        action_type = "ChSitSpin3"
    if action_type == "3S_1Eu_2S":
        action_type = "3Salchow_1Euler_2Salchow"
    if action_type == "3Filp_1Euler_3Salchpw":
        action_type = "3Filp_1Euler_3Salchow"
    if action_type == "FlySitSpin3_n98_p04_g10":
        action_type = "FlySitSpin3"
    if action_type == "4Toeloop_3Axel_SEQ":
        action_type = "4Toeloop_3Axel"
    if action_type == "4Lutz_n99_p11_g01":
        action_type = "4Lutz"

    if action_type == "3Loop_2Axel_SEQ":
        action_type = "3Loop_2Axel"
    if action_type == "3Lutz_2Axel_SEQ":
        action_type = "3Lutz_2Axel"
    if action_type == "3Flip_2Axel_SEQ":
        action_type = "3Flip_2Axel"
    if action_type == "2Axel_SEQ_3Salchow":
        action_type = "2Axel_3Salchow"
    if action_type == "2Salchow_1Axel_SEQ":
        action_type = "2Salchow_1Axel"
    if action_type == "3Loop_REP":
        action_type = "3Loop"
    if action_type == "2Axel_2Axel_SEQ":
        action_type = "2Axel_2Axel"
    if action_type == "2Flip_COMBO":
        action_type = "2Flip"
    if action_type == "3Toeloop_COMBO_2Toeloop":
        action_type = "3Toeloop_2Toeloop"
    if action_type == "1Lutz_1Toeloop_COMBO":
        action_type = "1Lutz_1Toeloop"
    if action_type == "3Salchow_COMBO":
        action_type = "3Salchow"
    if action_type == "3Lutz_COMBO_2Toeloop":
        action_type = "3Lutz_2Toeloop"
    if action_type == "1Flip_COMBO_1Toeloop":
        action_type = "1Flip_1Toeloop"
    if action_type == "3Flip_COMBO":
        action_type = "3Flip"
    if action_type == "3Toeloop_COMBO":
        action_type = "3Toeloop"
    if action_type == "2Salchow_COMBO":
        action_type = "2Salchow"
    if action_type == "3Flip_COMBO_2Toeloop":
        action_type = "3Flip_2Toeloop"
    if action_type == "2Toeloop_COMBO":
        action_type = "2Toeloop"
    if action_type == "1Lutz_COMBO":
        action_type = "1Lutz"
    if action_type == "2Lutz_COMBO":
        action_type = "2Lutz"
    if action_type == "3Lutz_Combo":
        action_type = "3Lutz"
    if action_type == "3Flip_Combo":
        action_type = "3Flip"
    if action_type == "3Salchow_Combo":
        action_type = "3Salchow"
    if action_type == "3Salchow_COMBO_2Toeloop":
        action_type = "3Salchow_2Toeloop"
    if action_type == "3Toeloop_REP":
        action_type = "3Toeloop"
    if action_type == "3Axel_REP":
        action_type = "3Axel"
    if action_type == "3Lutz_3Flip_REP":
        action_type = "3Lutz_3Flip"
    if action_type == "2Loop_1Axel_SEQ":
        action_type = "2Loop_1Axel"
    if action_type == " 3Toeloop":
        action_type = "3Toeloop"
    if action_type == " 3Toeloop_2Toeloop":
        action_type = "3Toeloop_2Toeloop"
    if action_type == " 3Loop_2Toeloop":
        action_type = "3Loop_2Toeloop"
    if action_type == "CCSp1":
        action_type = "ChComboSpin1"
    if action_type == "CCSp2":
        action_type = "ChComboSpin2"
    if action_type == "ChComnoSpin4":
        action_type = "ChComboSpin4"
    if action_type == "3Lutz_SEQ_2Toeloop":
        action_type = "3Lutz_2Toeloop"
    if action_type == "3Lutz_COMDO":
        action_type = "3Lutz"
    if action_type == "3Lutz_COMBO_3Toeloop":
        action_type = "3Lutz_3Toeloop"
    if action_type == "3Filp_REP":
        action_type = "3Filp"

    if action_type == "ChComolSpin4":
        action_type = "ChComboSpin4"
    if action_type == "ChComolSpin3":
        action_type = "ChComboSpin3"
    if action_type == "ChComolSpin2":
        action_type = "ChComboSpin2"
    if action_type == "FLyChComboSpin4":
        action_type = "FlyChComboSpin4"
    if action_type == "FLyChComboSpin3":
        action_type = "FlyChComboSpin3"
    if action_type == "FLyChComboSpin2":
        action_type = "FlyChComboSpin2"
    if action_type == "FlychComboSpin1":
        action_type = "FlyChComboSpin1"

    if action_type == "Ch Sit Spin3 ":
        action_type = "ChSitSpin3"
    if action_type == "3Tocloop2Tocloop":
        action_type = "3Toeloop_2Toeloop"
    if action_type == "Ch_Camel_Spin3":
        action_type = "ChCamelSpin3"
    if action_type == "ChCmoboSpin4":
        action_type = "ChComboSpin4"
    if action_type == "CSSp2":
        action_type = "ChSitSpin2"
    if action_type == "Step_Sequence2":
        action_type = "StepSequence2"
    if action_type == "1Filp":
        action_type = "1Flip"
    if action_type == "2Axel__3Toeloop":
        action_type = "2Axel_3Toeloop"
    if action_type == "2Filp_3Toeloop":
        action_type = "2Flip_3Toeloop"
    if action_type == "2Lutz_Euler_2Flip":
        action_type = "2Lutz_1Euler_2Flip"
    if action_type == "2Lutz_Euler_2Salchow":
        action_type = "2Lutz_1Euler_2Salchow"
    if action_type == "2Salchow_Euler_2Salchow":
        action_type = "2Salchow_1Euler_2Salchow"
    if action_type == "3Axel_Euler_2Salchow":
        action_type = "3Axel_1Euler_2Salchow"
    if action_type == "3Loop2Toeloop":
        action_type = "3Loop_2Toeloop"
    if action_type == "3Lutz ":
        action_type = "3Lutz"
    if action_type == "ChSiltSpin3":
        action_type = "ChSitSpin3"
    if action_type == "ChoreoSquence1":
        action_type = "ChoreoSequence1"
    if action_type == "ComolSpin2":
        action_type = "ComboSpin2"
    if action_type == "FiySitSpin3":
        action_type = "FlySitSpin3"
    if action_type == "FLyCamelSpin4":
        action_type = "FlyCamelSpin4"
    if action_type == "FlyCamelSpin 4":
        action_type = "FlyCamelSpin4"
    if action_type == "FlySitSpinn4":
        action_type = "FlySitSpin4"
    if action_type == "LaybackSpain2":
        action_type = "LaybackSpin2"
    if action_type == "LaybackSpinB":
        action_type = "LaybackSpin1"
    if action_type == "StepSquence":
        action_type = "StepSquence1"
    if action_type == "StepSquence3":
        action_type = "StepSequence3"
    if action_type == "Step_Sequence2":
        action_type = "StepSequence2"
    if action_type == "StepSquence1":
        action_type = "StepSequence1"
    if action_type == "2AxeI":
        action_type = "2Axel"
    if action_type == "3Lutz_1Euler_3Filp":
        action_type = "3Lutz_1Euler_3Flip"
    if action_type == "3Filp":
        action_type = "3Flip"
    if action_type == "3Filp_1Euler_2Salchow":
        action_type = "3Flip_1Euler_2Salchow"
    if action_type == "3Filp_1Euler_3Salchow":
        action_type = "3Flip_1Euler_3Salchow"
    if action_type == "3Filp_2Toeloop_2Loop":
        action_type = "3Flip_2Toeloop_2Loop"
    if action_type == "3Filp_3Toeloop":
        action_type = "3Flip_3Toeloop"
    if action_type == "3Axel_1Euler_3Filp":
        action_type = "3Axel_1Euler_3Flip"
    if action_type == "FlySitspin4":
        action_type = "FlySitSpin4"

    return action_type
def process(data,data_out_path,video_name):
    ##先处理第一个
    player = data[0, 0].split('/')[1]
    video_length = int(abs(data[0, 3] - data[0, 2]))
    action_type = data[0, 1]
    ground = []
    action_length = abs(data[0, 5] - data[0, 4])
    start_length = abs(data[0, 4] - data[0, 2])
    action_type = valid_action(action_type)# the valiation of action types
    ground.extend(['None']*start_length)
    ground.extend([action_type]*action_length)
    last = player
    ##then with processing
    for i in range(1,data.shape[0]):
        player = data[i,0].split('/')[1]
        if player == last:##with the same player
            action_type = data[i,1]
            action_type = valid_action(action_type)  # the valiation of action types
            start_length = abs(data[i,4]-data[i-1,5])
            action_length = abs(data[i, 5] - data[i, 4])
            ground.extend(['None']*start_length)
            ground.extend([action_type]*action_length)

            last = player
        else:##Change to other player
            ##writing down the data of last player
            if (len(ground) <= video_length):##It means the video is not finishing after action have been end, so it need to add 'None' frames.
                lack_length = video_length-len(ground)
                ground.extend(['None']*lack_length)
            else:## Some situations may be happen.
                a = len(ground)
                print("some errors happen")
                sys.exit()
            if(len(ground)==video_length): ##
                if not os.path.exists(data_out_path):
                    os.makedirs(data_out_path)
                data_out = '{}/{}_{}.txt'.format(data_out_path,video_name,last)
                try:
                    with open(data_out, 'w') as f:
                        for line in ground:
                            f.write(line + '\n')
                        f.close()
                except Exception as e:
                    print(e)
                    print("somthing error")
            else:
                print("some errors happen")
                sys.exit()
            ##restart
            print('datastart:',video_name)
            ground = []
            video_length = int(abs(data[i, 3] - data[i, 2]))
            action_type = data[i, 1]
            action_type = valid_action(action_type)  # the valiation of action types
            start_length = abs(data[i, 4] - data[i, 2])
            action_length = abs(data[i,5] - data[i,4])
            ground.extend(['None']*start_length)
            ground.extend([action_type]*action_length)
            last = player
    ## write in the last one, do not forget to add 'None' frames
    if (len(ground) <= video_length):  ##It means the video is not finishing after action have been end, so it need to add 'None' frames.
        lack_length = video_length - len(ground)
        ground.extend(['None'] * lack_length)
    else:  ## Some situations may be happen.
        print("some errors happen")
        sys.exit()
    if (len(ground) == video_length):  ##
        if not os.path.exists(data_out_path):
            os.makedirs(data_out_path)
        data_out = '{}/{}_{}.txt'.format(data_out_path, video_name, last)
        try:
            with open(data_out, 'w') as f:
                for line in ground:
                    f.write(line + '\n')
                f.close()
        except Exception as e:
            print(e)
    else:
        print("some errors happen")
        sys.exit()

if __name__ == '__main__':
    # data_path = 'Excel'
    # data_out_path = 'groundtrue'
    # root = os.listdir(data_path)[:-1]
    #
    # root.sort(key=lambda x: int((x.split('.')[0])[1:]))
    #
    # for file in root:
    #     data_in = os.path.join(data_path,file)
    #     data = pd.read_excel(data_in)
    #     data = np.array(data)
    #     video_name = file.split('.')[0]
    #     print(video_name)
    #     process(data,data_out_path,video_name)
    # print('sucessful')
    a = np.load('x77/n77_p01.npy')

    print(a.shape)

