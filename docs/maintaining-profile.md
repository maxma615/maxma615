# 维护这个主页

Profile README 与个人网站共用此仓库。网站数据集中在 `data.js`，页面结构和显示样式分别位于 `index.html`、`main.js` 与 `styles.css`。

更新经历时同步修改 README，并核对项目时间、个人职责及成果状态。推送到 `main` 后，GitHub Actions 自动发布至 [GitHub Pages](https://maxma615.github.io/maxma615/)。

本地验证与预览：

```bash
npm test
python3 -m http.server 4173
```

## README 封面

`assets/readme/hero-*.svg` 是仓库内的独立矢量封面，分别适配桌面、手机以及深浅主题。文字使用 Space Grotesk 转为轮廓，因此不需要访客安装字体或请求外部字体服务。字体源文件和 SIL Open Font License 位于 `assets/readme/fonts/`；来源为 [Google Fonts / Space Grotesk](https://github.com/google/fonts/tree/main/ofl/spacegrotesk)。

封面动效在 4.6 秒内结束。开启系统“减少动态效果”时，`picture` 会直接选择对应的 `*-static.svg`，这些文件不包含动画；动效版 SVG 内也有同一偏好的后备规则。链接与展开操作使用 GitHub 原生 Markdown / HTML，图片本身没有脚本。

修改封面后重新生成：

```bash
python3 -m pip install fonttools
python3 scripts/build-readme-assets.py
```

封面视觉参考：

- [Anthony Fu](https://github.com/antfu/antfu)：简洁的等宽文字导航。
- [Anurag Hazra](https://github.com/anuraghazra/anuraghazra)：统一的首屏视觉与项目展示。
- [Sindre Sorhus](https://github.com/sindresorhus/sindresorhus)：少量本地动图带来的个人风格。

封面、机械臂线稿与动画为本仓库制作，未使用这些主页的图片或代码。
