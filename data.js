export const portfolioData = {
  profile: {
    name: 'Max.Ma',
    role: '智能科学与技术 · AI / Robotics / CV',
    location: 'Hangzhou Dianzi University · 中国',
    intro: '专注于计算机视觉、机器人与边缘端 AI。这里记录我在开源工具、真实机器人系统与技术探索中的工作。',
    email: 'maxma615@users.noreply.github.com',
    github: 'https://github.com/maxma615'
  },
  achievements: [
    { year: '2025', award: '全国一等奖', event: '全国大学生计算机设计大赛', detail: '以智能交互作品完成从方案到演示的完整交付。' },
    { year: '2024', award: '金奖', event: '中国国际大学生创新大赛', detail: '负责技术方案、核心原型与项目路演。' },
    { year: '2024', award: '区域赛银奖', event: 'ACM-ICPC 程序设计竞赛', detail: '专注算法建模、协作解题与赛后复盘。' },
    { year: '2023', award: '优秀项目奖', event: '开源创新挑战赛', detail: '将开发工具贡献为可复用的开源项目。' }
  ],
  projects: [
    { index: '01', title: 'racing_vision_ai', description: '基于 ROS 2 的视觉事件系统：接收赛道信号并调用视觉语言模型分析目标帧，将感知结果接入真实机器人工作流。', role: 'ROS 2 · Computer Vision', tags: ['ROS 2', 'Python', 'VLM'], link: 'https://github.com/maxma615/racing_vision_ai', linkLabel: '查看仓库' },
    { index: '02', title: 'rdk_LeRobot_tools', description: '面向 LeRobot 的 BPU 工具集，探索具身智能模型在 RDK 硬件上的工程化运行与部署支持。', role: 'Edge AI · Tooling', tags: ['C++', 'LeRobot', 'RDK'], link: 'https://github.com/maxma615/rdk_LeRobot_tools', linkLabel: '查看仓库' },
    { index: '03', title: 'Skills', description: '一套持续演进的个人 AI 编程与研究工作流技能库，让重复性任务沉淀为可复用的工具与方法。', role: 'Developer Experience · Open Source', tags: ['Python', 'AI Agents', 'Tools'], link: 'https://github.com/maxma615/skills', linkLabel: '查看仓库' }
  ],
  skills: [
    { label: '构建', items: ['JavaScript / TypeScript', 'Python', 'Web 前端', '工程化'] },
    { label: '探索', items: ['机器学习', '计算机视觉', '算法与数据结构', '快速原型'] },
    { label: '表达', items: ['产品思维', '技术写作', '项目路演', '开源协作'] }
  ]
};
