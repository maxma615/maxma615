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
