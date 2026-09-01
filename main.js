import { portfolioData } from './data.js';

const createElement = (tag, className, text) => {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text) element.textContent = text;
  return element;
};

const createAchievement = ({ year, award, event, detail }) => {
  const item = createElement('li', 'achievement-item');
  item.append(createElement('span', 'achievement-year', year), createElement('strong', 'achievement-award', award));
  const copy = createElement('div', 'achievement-copy');
  copy.append(createElement('h3', '', event), createElement('p', '', detail));
  item.append(copy);
  return item;
};

const createProject = ({ index, title, description, role, tags, link, linkLabel }) => {
  const card = createElement('article', 'project-card');
  const top = createElement('div', 'project-top');
  top.append(createElement('span', 'project-index', index), createElement('span', 'project-role', role));
  const heading = createElement('h3', '', title);
  const tagList = createElement('ul', 'tag-list');
  tags.forEach((tag) => tagList.append(createElement('li', '', tag)));
  const anchor = createElement('a', 'text-link', `${linkLabel} ↗`);
  anchor.href = link;
  if (link.startsWith('http')) { anchor.target = '_blank'; anchor.rel = 'noreferrer'; }
  card.append(top, heading, createElement('p', 'project-description', description), tagList, anchor);
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
  document.querySelector('#email-link').href = `mailto:${data.profile.email}`;
  document.querySelector('#email-link').firstChild.textContent = `${data.profile.email} `;
  document.querySelector('#github-link').href = data.profile.github;
  document.querySelector('#achievements-list').replaceChildren(...data.achievements.map(createAchievement));
  document.querySelector('#projects-list').replaceChildren(...data.projects.map(createProject));
  document.querySelector('#skills-list').replaceChildren(...data.skills.map(createSkillGroup));
}

renderPortfolio(portfolioData);
document.querySelector('#current-year').textContent = new Date().getFullYear();
