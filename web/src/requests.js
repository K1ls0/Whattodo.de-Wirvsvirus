const TAGS_URL = '/tags';
const ELEM_INTERACTION_URL = '/elements';

resp = null; // Make more secure

function requestTags() {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        global resp;
        resp = xhr.responseText();
    });

    xhr.open('GET', TAGS_URL);
    xhr.send();
    // TODO return as structure
    return JSON.parse(resp);
}

function getIdeasByFilter(tagArr, doInclude) {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        if (this)
        global resp;
        resp = xhr.responseText();
    });

    xhr.open('GET', ELEM_INTERACTION_URL);
    xhr.send(JSON.stringify(tags: tagArr, include: doInclude));

    return JSON.parse(resp); // TODO return as structure
}

function pushNewIdea(ideaText, tagArr) {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        global resp;
        resp = xhr.responseText();
    });
    //Prepare json string manually (Javascript cannot do that)
    let tagsAsStr ='[';
    for (let i = 0; i < tagArr.length; i++) {
        tagsAsStr +='"' + tagArr[i] + '"'
        if (i != (tagArr.length - 1)) {
            tatgsAsStr += ','
        }

    }
    tagsAsStr += ']';

    xhr.open('PUT', ELEM_INTERACTION_URL);
    xhr.send('{"' + ideaText + '":' + tagsAsStr + '}');

    return JSON.parse(resp); // TODO return as structure
}