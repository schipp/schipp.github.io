function createElement(type, classNames, text = '') {
    const element = document.createElement(type);
    if (classNames) element.classList.add(...classNames.split(' '));
    if (text) element.textContent = text;
    return element;
}

function generateGrid(papers, gridType) {
    const gridContainer = createElement('div', 'grid-container');

    Object.entries(papers).forEach(([id, paper]) => {
        const gridItem = createElement('div', 'grid-item');
        const img = createElement('img', 'image');
        img.src = paper.preview_img;

        const overlayImage = createElement('div', 'overlay-image');
        overlayImage.appendChild(img);

        if (paper.tag === 'new') {
            overlayImage.appendChild(createElement('h3', null, 'NEW'));
        }

        if (gridType === 'papers') {
            overlayImage.appendChild(createElement('journal', null, `${paper.journal}, ${paper.year}`));
        }

        const title = createElement('div', 'text', paper.title);
        const link = createElement('a', null);
        link.href = paper.url;
        link.append(overlayImage, title);
        gridItem.appendChild(link);

        gridContainer.appendChild(gridItem);
    });

    return gridContainer;
}

fetch("data.json")
    .then(response => response.json())
    .then(data => {
        const { publications, repositories } = data;
        const papersGridContainer = generateGrid(publications, 'papers');
        const githubGridContainer = generateGrid(repositories, 'repositories');
        document.querySelector('.paper_grid').appendChild(papersGridContainer);
        document.querySelector('.github_grid').appendChild(githubGridContainer);
    });
