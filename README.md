# Max.Ma · 马超

**Robotics · Computer Vision · Edge AI**

把模型部署、硬件调试和应用开发连接成可以实际运行的系统。

[个人主页 ↗](https://maxma615.github.io/maxma615/) · [开源仓库 ↗](https://github.com/maxma615?tab=repositories)

---

我在杭州电子科技大学学习**智能科学与技术（Intelligent Science and Technology）**，2022 年入学。2025 年在**地瓜机器人 D-Robotics** 开发者生态部实习，担任**机器人应用开发实习生**，参与 RDK 平台的模型部署、机械臂应用、技术文档与开发者支持。

*以下经历更新至 2025 年 9 月。*

## 实习与工程实践

- **LeRobot / ACT 机械臂**：协助完成 RDK S100 上的 ACT 叠衣服演示与全流程文档；在 ROS 暑期学校支持 ACT 量化部署和 ONNX / HBM 推理精度验证。
- **RDK S100 Model Zoo**：参与 MobileNet、ResNet、EfficientNet-Lite 和 ByteTrack 的上库工作，编写量化部署说明、示例与 x86 / S100 推理验证脚本，完成 ImageNet 验证集精度验证。
- **机械臂接口与视觉抓取**：调研机械臂 API / SDK，完成 LeRobot 接口集成，并设计结合 YOLOv8、FastSAM、PCA 的不规则积木抓取方案。
- **RDK X5 小智 AI**：完成协议验证与平台适配，跑通语音对话、天气搜索和音乐搜索。
- **文档与开发者支持**：维护 RDK 中英文手册，整理资源与 FAQ，完成图片迁移及离线下载、链接替换脚本；参与创业森林、AdventureX、ROS 暑期学校和智能车赛事的技术支持与现场协作。

## 竞赛与学习

| 时间 | 竞赛 | 成绩 |
| :--- | :--- | :--- |
| 2025.01 | 全国大学生物理实验竞赛 | 全国三等奖 · 浙江省一等奖 |
| 2024.12 | 全国大学生智能车竞赛 · 5G 远程组 | 全国一等奖 · 第三名 |
| 2024.09 | 全国大学生智能车竞赛 · 地平线智慧医疗组 | 全国一等奖 · 第三名 |
| 2023.08 | 全国大学生机器人创意大赛 | 全国二等奖 |

2024 年获校一等奖学金两次，2025 年获校二等奖学金一次。

## 开源项目与协作

- [**racing_vision_ai**](https://github.com/maxma615/racing_vision_ai) — ROS 2 赛道视觉事件分析：按信号采集图像，调用视觉语言模型并接入机器人工作流。
- [**rdk_LeRobot_tools**](https://github.com/maxma615/rdk_LeRobot_tools) — D-Robotics 项目的 fork，记录参与的 RDK BPU 工具与 LeRobot ACT 部署工作。
- [**RDK S100 Model Zoo**](https://github.com/D-Robotics/rdk_model_zoo_s) — 参与的上游模型部署项目，包含模型示例、量化流程与精度验证。
- **RDK 节点使用文档** — [YOLO](https://github.com/maxma615/nodehub_YOLO)、[语音识别](https://github.com/maxma615/nodehub_asr)、[语音合成](https://github.com/maxma615/nodehub_tts) 等组件的使用指南与部署说明。

## 技术与工具

- **常用**：Python、Linux、ROS / ROS 2、Git、Markdown。
- **工程实践**：RDK 模型量化与部署、计算机视觉、LeRobot / ACT、模型精度验证。
- **基础与接触**：C / C++、PyTorch、STM32、51 单片机、PCB 设计。
- **协作**：技术文档、问题复现与排查、开发者培训、竞赛与活动支持。

欢迎围绕机器人、视觉和边缘端 AI 交流。[在 GitHub 找到我 ↗](https://github.com/maxma615)

<details>
<summary>维护这个主页</summary>

Profile README 与个人网站共用此仓库。网站数据集中在 `data.js`，页面结构和显示样式分别位于 `index.html`、`main.js` 与 `styles.css`。

更新经历时同步修改 README，并核对项目时间、个人职责及成果状态。推送到 `main` 后，GitHub Actions 自动发布至 [GitHub Pages](https://maxma615.github.io/maxma615/)。

本地验证与预览：

```bash
npm test
python3 -m http.server 4173
```

</details>
