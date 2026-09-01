export const portfolioData = {
  profile: {
    name: '你的名字',
    role: '开发者 · 竞赛选手 · 创作者',
    location: '中国 · 可远程协作',
    intro: '我把复杂问题拆解成可落地的产品、算法与体验。这里记录我的比赛、项目与持续探索。',
    email: 'hello@example.com',
    github: 'https://github.com/maxma615'
  },
  achievements: [
    { year: '2025', award: '全国一等奖', event: '全国大学生计算机设计大赛', detail: '以智能交互作品完成从方案到演示的完整交付。' },
    { year: '2024', award: '金奖', event: '中国国际大学生创新大赛', detail: '负责技术方案、核心原型与项目路演。' },
    { year: '2024', award: '区域赛银奖', event: 'ACM-ICPC 程序设计竞赛', detail: '专注算法建模、协作解题与赛后复盘。' },
    { year: '2023', award: '优秀项目奖', event: '开源创新挑战赛', detail: '将开发工具贡献为可复用的开源项目。' }
  ],
  projects: [
    { index: '01', title: '智能学习助手', description: '面向复杂知识整理的 AI 应用，把资料提炼、任务分解与学习反馈组织为流畅的一条工作流。', role: '产品设计 · 全栈开发', tags: ['LLM', 'React', 'Python'], link: '#contact', linkLabel: '查看合作方式' },
    { index: '02', title: '视觉检测系统', description: '从数据标注到边缘部署的视觉识别方案，用于更快、更稳定地发现真实场景中的关键目标。', role: '算法工程 · 部署优化', tags: ['Computer Vision', 'ONNX', 'Edge AI'], link: '#achievements', linkLabel: '查看竞赛实践' },
    { index: '03', title: '开源开发工具', description: '将重复的工程工作变成清晰、可复用的命令与模板，帮助团队更专注于真正重要的问题。', role: '开发者体验 · 开源维护', tags: ['Node.js', 'CLI', 'Open Source'], link: 'https://github.com/maxma615', linkLabel: '访问 GitHub' }
  ],
  skills: [
    { label: '构建', items: ['JavaScript / TypeScript', 'Python', 'Web 前端', '工程化'] },
    { label: '探索', items: ['机器学习', '计算机视觉', '算法与数据结构', '快速原型'] },
    { label: '表达', items: ['产品思维', '技术写作', '项目路演', '开源协作'] }
  ]
};
