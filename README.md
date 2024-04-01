# NetGuardian
Source Code for NetGuardian

Step1.先运行read_log.py,该脚本包括对Zeek log的解析和一些特征的提取
Step2.其次运行dfs_pre.py,用于将Zeek log转化成图形式
Step3.feature.py用于提取历史特征，process.py用于节点聚类
Step4.lm_scan.py、c2_*.py、de_*.py、slice.py分别是四个Stage Detector（另外Learn.py用于训练钓鱼邮件检测模型）
Step5:link_dig.py用于挖掘异常节点以及评分
Step6:nulctrl.py用于生成攻击路径

其他：
database.py用于处理ecar数据
Statistical.py和QZA.py用于数据集中一些信息的统计和画图
mergecopy2.py data merge算法
