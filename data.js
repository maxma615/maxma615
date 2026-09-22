// Experience is a September 2025 snapshot; later repository activity is not a project date.
export const portfolioData = {
  asOf: '2025.09',
  profile: {
    name: 'Max.Ma',
    role: '机器人应用开发 · 边缘端 AI',
    location: '杭州电子科技大学 · 智能科学与技术',
    intro: '你好，我是马超。关注机器人、计算机视觉与边缘端 AI，喜欢把模型部署、硬件调试和应用开发连接成一个可以实际运行的系统。',
    bio: '2022 年进入杭州电子科技大学学习智能科学与技术。2025 年在地瓜机器人开发者生态部实习，参与 RDK 平台的模型部署、机械臂应用、技术文档与开发者支持。',
    github: 'https://github.com/maxma615'
  },
  highlights: [
    { value: 'RDK S100 / X5', label: '边缘端模型与应用' },
    { value: 'ROS / ROS 2', label: '机器人开发与集成' },
    { value: 'LeRobot · ACT', label: '机械臂与模仿学习实践' }
  ],
  experience: [
    {
      period: '2025',
      title: '地瓜机器人 D-Robotics',
      role: '机器人应用开发实习生 · 开发者生态部',
      details: [
        '参与 RDK S100 模型量化、部署与精度验证，以及 LeRobot 机械臂应用开发。',
        '完成 RDK X5 小智 AI 协议验证与适配，跑通语音对话、天气和音乐搜索。',
        '维护 RDK 中英文手册，整理资源与 FAQ；完成文档图片迁移，并提供离线下载和链接替换脚本。',
        '参与创业森林、AdventureX、ROS 暑期学校及智能车省赛、国赛的技术支持与现场协作。'
      ]
    },
    {
      period: '2022.09',
      title: '杭州电子科技大学',
      role: '智能科学与技术 · 本科阶段',
      details: [
        '围绕机器视觉、深度学习、自动控制与智能机器人开展学习，将技术实践与智能车竞赛结合。',
        '2024 年获校一等奖学金两次，2025 年获校二等奖学金一次。'
      ]
    }
  ],
  achievements: [
    { year: '2025.01', award: '全国三等奖', event: '全国大学生物理实验竞赛', detail: '同时获浙江省一等奖。' },
    { year: '2024.12', award: '全国一等奖 · 第三名', event: '全国大学生智能车竞赛', detail: '5G 远程组。' },
    { year: '2024.09', award: '全国一等奖 · 第三名', event: '全国大学生智能车竞赛', detail: '地平线智慧医疗组。' },
    { year: '2023.08', award: '全国二等奖', event: '全国大学生机器人创意大赛', detail: '机器人竞赛实践。' }
  ],
  projects: [
    {
      index: '01',
      title: 'LeRobot 机械臂实践',
      repository: 'rdk_LeRobot_tools · D-Robotics fork',
      description: '参与 RDK S100 上基于 LeRobot ACT 的叠衣服演示，协助打通全流程并沉淀部署文档。',
      outcome: '在 ROS 暑期学校支持 ACT 量化部署，验证 ONNX 与 HBM 模型的推理精度。',
      role: '协作开发 · 2025',
      tags: ['RDK S100', 'LeRobot', 'ACT', '模型量化'],
      link: 'https://github.com/maxma615/rdk_LeRobot_tools',
      linkLabel: '查看工具与部署文档'
    },
    {
      index: '02',
      title: 'RDK S100 Model Zoo',
      repository: 'D-Robotics / rdk_model_zoo_s',
      description: '参与 MobileNet、ResNet、EfficientNet-Lite 与 ByteTrack 的上库工作，编写量化部署说明与示例。',
      outcome: '完成 ImageNet 验证集精度验证，补充 x86 与 S100 端推理验证脚本。',
      role: '模型部署 · 2025',
      tags: ['Computer Vision', 'BPU', 'ImageNet', 'Python'],
      link: 'https://github.com/D-Robotics/rdk_model_zoo_s',
      linkLabel: '查看参与的上游项目'
    },
    {
      index: '03',
      title: '视觉引导机械臂抓取',
      description: '调研机械臂 API 与 SDK，完成 LeRobot 接口集成，并设计不规则乐高积木抓取方案。',
      outcome: '方案结合 YOLOv8 目标检测、FastSAM 分割与 PCA 位姿估计，探索视觉引导的抓取流程。',
      role: '接口集成与方案设计 · 2025',
      tags: ['YOLOv8', 'FastSAM', 'PCA', '机械臂']
    },
    {
      index: '04',
      title: '赛道视觉事件分析',
      repository: 'racing_vision_ai',
      description: '接收 ROS 2 赛道信号，在指定状态采集图像，调用视觉语言模型完成图像理解。',
      outcome: '将事件触发、相机图像与模型分析接入机器人工作流。',
      role: '开源项目',
      tags: ['ROS 2', 'Python', 'VLM'],
      link: 'https://github.com/maxma615/racing_vision_ai',
      linkLabel: '查看项目源码'
    }
  ],
  skills: [
    { label: '开发与协作', items: ['Python · Linux', 'ROS / ROS 2', 'Git · Markdown', 'C / C++（基础）'] },
    { label: '模型与机器人', items: ['RDK 模型量化与部署', '计算机视觉 · 精度验证', 'LeRobot / ACT 应用实践', 'PyTorch（基础）'] },
    { label: '文档与支持', items: ['中英文技术文档维护', '问题复现与排查', '开发者培训与社区支持', '竞赛与活动现场协作'] }
  ]
};
