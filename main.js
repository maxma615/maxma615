import { portfolioData } from './data.js';

const createElement = (tag, className, text) => {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text) element.textContent = text;
  return element;
};

const createHighlight = ({ value, label }) => {
  const item = createElement('li', 'highlight-item');
  item.append(createElement('strong', 'highlight-value', value), createElement('span', 'highlight-label', label));
  return item;
};

const createExperience = ({ period, title, role, details }) => {
  const item = createElement('li', 'experience-item');
  const copy = createElement('div', 'experience-copy');
  const list = createElement('ul', 'experience-details');
  details.forEach((detail) => list.append(createElement('li', '', detail)));
  copy.append(createElement('h3', '', title), createElement('p', 'experience-role', role), list);
  item.append(createElement('span', 'experience-period', period), copy);
  return item;
};

const createAchievement = ({ year, award, event, detail }) => {
  const item = createElement('li', 'achievement-item');
  item.append(createElement('span', 'achievement-year', year), createElement('strong', 'achievement-award', award));
  const copy = createElement('div', 'achievement-copy');
  copy.append(createElement('h3', '', event), createElement('p', '', detail));
  item.append(copy);
  return item;
};

const createProject = ({ index, title, repository, description, outcome, role, tags, link, linkLabel }) => {
  const card = createElement('article', 'project-card');
  const top = createElement('div', 'project-top');
  top.append(createElement('span', 'project-index', index), createElement('span', 'project-role', role));
  const tagList = createElement('ul', 'tag-list');
  tags.forEach((tag) => tagList.append(createElement('li', '', tag)));
  card.append(top, createElement('h3', '', title));
  if (repository) card.append(createElement('p', 'project-repository', repository));
  card.append(createElement('p', 'project-description', description));
  if (outcome) card.append(createElement('p', 'project-outcome', outcome));
  card.append(tagList);
  if (link) {
    const anchor = createElement('a', 'text-link', `${linkLabel} ↗`);
    anchor.href = link;
    anchor.target = '_blank';
    anchor.rel = 'noopener noreferrer';
    anchor.setAttribute('aria-label', `${title}：${linkLabel}（新窗口打开）`);
    card.append(anchor);
  }
  return card;
};

const createSkillGroup = ({ label, items }) => {
  const group = createElement('section', 'skill-group');
  group.append(createElement('h3', '', label));
  const list = createElement('ul', 'skill-list');
  items.forEach((item) => list.append(createElement('li', '', item)));
  group.append(list);
  return group;
};

export function renderPortfolio(data) {
  document.querySelector('#profile-name').textContent = data.profile.name;
  document.querySelector('#profile-role').textContent = data.profile.role;
  document.querySelector('#profile-location').textContent = data.profile.location;
  document.querySelector('#profile-intro').textContent = data.profile.intro;
  document.querySelector('#profile-bio').textContent = data.profile.bio;
  document.querySelector('#content-as-of').textContent = `经历更新至 ${data.asOf}`;
  document.querySelector('#github-link').href = data.profile.github;
  document.querySelector('#highlights-list').replaceChildren(...data.highlights.map(createHighlight));
  document.querySelector('#experience-list').replaceChildren(...data.experience.map(createExperience));
  document.querySelector('#achievements-list').replaceChildren(...data.achievements.map(createAchievement));
  document.querySelector('#projects-list').replaceChildren(...data.projects.map(createProject));
  document.querySelector('#skills-list').replaceChildren(...data.skills.map(createSkillGroup));
  document.querySelectorAll('[data-portfolio-content]').forEach((element) => { element.hidden = false; });
  document.querySelector('#content-fallback').hidden = true;
}

renderPortfolio(portfolioData);
document.querySelector('#current-year').textContent = new Date().getFullYear();

// Keep the section marker useful for keyboard navigation and manual scrolling.
const navigation = [...document.querySelectorAll('.profile-nav a')].map((link) => ({
  link,
  section: document.querySelector(link.getAttribute('href'))
})).filter(({ section }) => section);

let scheduled = false;
function updateCurrentSection() {
  let current = navigation[0];
  const threshold = Math.min(window.innerHeight * 0.3, 200);
  for (const entry of navigation) {
    if (entry.section.getBoundingClientRect().top <= threshold) current = entry;
  }
  if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
    // The last two anchors may share the same scroll position on tall screens.
    const requested = navigation.find(({ link, section }) => {
      const top = section.getBoundingClientRect().top;
      return link.hash === window.location.hash && top >= 0 && top < window.innerHeight;
    });
    current = requested || navigation.at(-1);
  }
  for (const entry of navigation) {
    if (entry === current) entry.link.setAttribute('aria-current', 'location');
    else entry.link.removeAttribute('aria-current');
  }
  scheduled = false;
}
function scheduleSectionUpdate() {
  if (!scheduled) {
    scheduled = true;
    requestAnimationFrame(updateCurrentSection);
  }
}
window.addEventListener('scroll', scheduleSectionUpdate, { passive: true });
window.addEventListener('resize', scheduleSectionUpdate);
window.addEventListener('load', scheduleSectionUpdate);
window.addEventListener('hashchange', scheduleSectionUpdate);
updateCurrentSection();
