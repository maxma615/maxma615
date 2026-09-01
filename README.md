# Personal Portfolio

一个可部署到 GitHub Pages 的中文个人展示站点，用来介绍自己、展示比赛成绩与项目。

## 更新内容

所有需要替换的资料都在 `data.js`：

- `profile`：姓名、定位、简介、邮箱和 GitHub 链接。
- `achievements`：比赛年份、奖项、赛事和一句说明。
- `projects`：项目名称、描述、角色、技术标签与链接。
- `skills`：能力分类与标签。

更新后执行：

```bash
npm test
git add .
git commit -m "update: refresh portfolio content"
git push
```

## 启用 GitHub Pages

1. 打开仓库的 **Settings → Pages**。
2. 在 **Build and deployment** 中选择 **GitHub Actions**。
3. 推送到 `main` 分支后，等待名为 **Deploy portfolio to GitHub Pages** 的工作流完成。

本站发布地址：`https://machao615.github.io/personal-portfolio/`。

## 本地检查

```bash
npm test
npx --yes serve .
```
