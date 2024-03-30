import os

if True:
    # ====================================先将resource相关文件进行编译=======================================
    # =============================================================================
    # 编译resuource文件至py
    # =============================================================================
    resName = 'picture'
    rescmd = f"D:\ProgramFiles\miniconda3\Scripts\pyrcc5.exe UI/openBMP/{resName}.qrc -o Resources/Icons/{resName}_rc.py"
    os.system(rescmd)
    # os.popen(rescmd)

if False:
    # =============================================================================
    # 编译openBMP.ui至py文件
    # =============================================================================
    uiName = "OpenBMP"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o Main/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件
    
if True:
    # =============================================================================
    # 编译LocalBlastGUI.ui至py文件
    # =============================================================================
    uiName = "LocalBlastGUI"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o Blast/BlastGUI/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    # =============================================================================
    # 编译MolarityCalculator.ui至py文件
    # =============================================================================
    uiName = "RenameID"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o ToolBox/RenameID/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    # =============================================================================
    # 编译MolarityCalculator.ui至py文件
    # =============================================================================
    uiName = "MolarityCalculator"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o ToolBox/MolarityCalculator/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件
    
    # =============================================================================
    # 编译LigationCalculator.ui至py文件
    # =============================================================================
    uiName = "LigationCalculator"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o ToolBox/LigationCalculator/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件
    
    # =============================================================================
    # 编译amplicon.ui至py文件
    # =============================================================================
    uiName = "amplicon"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o Amplicon/Qiime/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    # =============================================================================
    # Matplotlib.ui至py文件
    # =============================================================================
    uiName = "Matplotlib"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o ToolBox/Matplotlib/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    # =============================================================================
    # PGAP.ui至py文件
    # =============================================================================
    uiName = "PGAP"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o Annotation/PGAP/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    # =============================================================================
    # MarkPDF.ui至py文件
    # =============================================================================
    uiName = "MarkPDF"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o ToolBox/MarkPDF/{uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

    print('编译中...')

if __name__ == '__main__':
    print(f'编译完成。')
