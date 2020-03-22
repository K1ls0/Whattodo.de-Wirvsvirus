const TAGS_URL = '/tags';
const ELEM_INTERACTION_URL = '/elements';

let resp = null; // Make more secure

export function requestTags(handlingFunction, thisC) {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        if (xhr.status != 200) {
            handlingFunction(null, thisC);
        } else {
            handlingFunction(JSON.parse(xhr.responseText), thisC);
        }
    });

    xhr.open('GET', TAGS_URL);
    xhr.send();
}

export function getIdeasByFilter(tagArr, doInclude, handlingFunction, thisC) {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        if (xhr.status != 200) {
            handlingFunction(null, thisC);
        } else {
            handlingFunction(JSON.parse(xhr.responseText), thisC);
        }
    });

    xhr.open('GET', ELEM_INTERACTION_URL);
    xhr.send(JSON.stringify({tags: tagArr, include: doInclude}));
}

export function pushNewIdea(ideaText, tagArr, handlingFunction, thisC) {
    let xhr = new XMLHttpRequest();
    resp = null;
    xhr.addEventListener('load', () => {
        if (xhr.status != 200) {
            handlingFunction(null, thisC);
        } else {
            handlingFunction(JSON.parse(xhr.responseText), thisC);
        }
    });
    //Prepare json string manually (Javascript cannot do that)
    let tagsAsStr ='[';
    for (let i = 0; i < tagArr.length; i++) {
        tagsAsStr +='"' + tagArr[i] + '"'
        if (i !== (tagArr.length - 1)) {
            tagsAsStr += ','
        }

    }
    tagsAsStr += ']';

    xhr.open('PUT', ELEM_INTERACTION_URL);
    xhr.send('{"' + ideaText + '":' + tagsAsStr + '}');
}