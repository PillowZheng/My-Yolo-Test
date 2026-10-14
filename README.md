# My-Yolo-Test
this where I record how I try to use yolo.
# 面试任务记录：本地大模型与YOLO视觉初探

## 关于我
非科班小白，正在努力学习AI基础。

## 任务一：本地部署大模型并接入应用
- **工具**：Ollama + Cherry Studio
- **模型**：Qwen2.5:1.5b（对比了WatamRole，发现小参数中文模型更适合我）
- **踩坑与解决**：
  - C盘空间不足，通过设置环境变量 `OLLAMA_MODELS` 将模型迁移至D盘。
  - GitHub网络受限导致模型下载卡顿，通过国内镜像/网盘替代方案解决。
- **成果**：成功通过API接入Cherry Studio，配置了带在线搜索的简易智能体。

## 任务二：YOLO目标检测跑通
- **工具**：VS Code + Python + ultralytics
- **数据集/权重**：官方预训练权重 `yolov8n.pt`（因GitHub限制，手动下载后本地加载）
- **成果**：成功运行官方示例 `bus.jpg`，输出检测结果 `result.jpg`（见仓库）。

## 学习感悟
虽然经历了环境配置、网络限制等重重困难，但通过拆分问题、寻找国内替代方案，我成功跑通了从大模型接入到视觉算法的初步流程，对接下来的AI学习充满期待。
