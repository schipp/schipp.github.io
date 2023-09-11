// populate the page from the data in json
// first time writing javascript, probably a huge mess

function generate_grid(papers, grid_type) {
    var grid_container = document.createElement("div");
    grid_container.classList.add("grid-container")
    for (var id in papers) {
        // grid container
        var grid_item = document.createElement("div");
        grid_item.classList.add("grid-item");
        // preview image
        var img = document.createElement("img");
        img.classList.add("image");
        img.src = papers[id]["preview_img"];
        var overlay_image = document.createElement("div");
        overlay_image.classList.add("overlay-image");
        overlay_image.appendChild(img);

        if (papers[id]["tag"] == "new") {
            var h3 = document.createElement("h3");
            h3.innerText = "NEW";
        }

        if (papers[id]["tag"] == "new") {
            overlay_image.appendChild(h3);
        }

        //  journal + year overlay ontop of image
        if (grid_type == "papers") {
            var journal = document.createElement("journal");
            journal.innerText = papers[id]["journal"] + ", " + papers[id]["year"];
            overlay_image.appendChild(journal);
        }

        // name of paper/repository
        var title = document.createElement("div");
        title.classList.add("text");
        title.innerText = papers[id]["title"]

        // href so everythings is a link
        var a = document.createElement("a");
        a.href = papers[id]["url"];
        a.appendChild(overlay_image);
        a.appendChild(title);
        grid_item.appendChild(a);

        grid_container.appendChild(grid_item);
    }
    return grid_container
}

fetch("data.json")
    .then(response => response.json())
    .then(data => {
        var papers = data["publications"];
        var repositories = data["repositories"];
        grid_container_papers = generate_grid(papers, "papers")
        grid_container_github = generate_grid(repositories, "repositories")
        document.getElementsByClassName("paper_grid")[0].appendChild(grid_container_papers)
        document.getElementsByClassName("github_grid")[0].appendChild(grid_container_github)
    })