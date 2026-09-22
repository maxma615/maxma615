# 维护这个主页

Profile README 与个人网站共用此仓库。网站数据集中在 `data.js`，页面结构和显示样式分别位于 `index.html`、`main.js` 与 `styles.css`。

更新经历时同步修改 README，并核对项目时间、个人职责及成果状态。推送到 `main` 后，GitHub Actions 自动发布至 [GitHub Pages](https://maxma615.github.io/maxma615/)。

本地验证与预览：

```bash
npm test
python3 -m http.server 4173
```

## README 动效与图片

`assets/readme/hero-*.svg` 为边缘计算芯片封面，`pipeline-*.svg` 为部署流程，`card-*.svg` 为四个项目的小动画。图片均为独立矢量文件，适配深浅主题；封面与流程另有手机排版。文字使用 Space Grotesk 转为轮廓，因此不需要访客安装字体或请求外部字体服务。字体源文件和 SIL Open Font License 位于 `assets/readme/fonts/`；来源为 [Google Fonts / Space Grotesk](https://github.com/google/fonts/tree/main/ofl/spacegrotesk)。

六个视觉区块持续循环播放，呈现数据传输、芯片计算、模型量化、视觉检测和开发者文档。图形仅作示意，不代表实时运行状态或性能测量。开启系统“减少动态效果”时，`picture` 会直接选择对应的 `*-static.svg`，这些文件不包含动画；动效版 SVG 内也有同一偏好的后备规则。链接与展开操作使用 GitHub 原生 Markdown / HTML，图片本身没有脚本。

修改封面后重新生成：

```bash
python3 -m pip install fonttools
python3 scripts/build-readme-assets.py
```

封面视觉参考：

- [Anthony Fu](https://github.com/antfu/antfu)：简洁的等宽文字导航。
- [Anurag Hazra](https://github.com/anuraghazra/anuraghazra)：统一的首屏视觉与项目展示。
- [Sindre Sorhus](https://github.com/sindresorhus/sindresorhus)：通过多处循环动图表达个人风格。

封面、芯片、流程与项目动画为本仓库原创制作，未使用这些主页的图片或代码。

## 个人站的内容顺序

首页依次展示个人介绍、项目、博客。实习经历、获奖和技能收在个人介绍的展开区；`asOf` 只表示经历资料的截止时间，不限制博客文章的发布日期。

项目在 `data.js` 的 `projects` 中维护。`artwork` 使用 `models`、`quantization`、`docs` 或 `vision`，对应仓库内的项目动图，系统减少动态效果时自动换成静态版本。

博客在 `data.js` 的 `articles` 中维护，每篇包含 `title`（原文标题）、`summary`（准确摘要）、`url`（原文地址），以及可选的 `date`（YYYY-MM-DD）、`platform`、`tags`。只加入已确认由本人撰写的文章；文章可按希望展示的顺序排列。没有确认文章时显示整理中的说明，不生成示例文章或把参与维护的项目文档当作本人博客。

文章打开原文地址，保留原来的发布平台。以后新增文章只需补充这一组内容，不必调整页面布局。

发布内容或样式更新时，同步递增 `index.html` 与 `main.js` 中的资源版本参数，避免已访问过网站的浏览器沿用旧缓存。
