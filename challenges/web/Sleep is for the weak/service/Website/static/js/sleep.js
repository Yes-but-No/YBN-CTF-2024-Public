const urlParams = new URLSearchParams(window.location.search);
const limit = urlParams.get('limit');
var scheduleCount = 1;
function createScheduleCard(startDateTime, endDateTime, description, scheduleID) {
    async function postEdit(data) {
        const result = await postRequest('backend/update_schedule.php', data);
        if (result.error){
            alert(result.error)
        }
    }
    // Convert startDateTime and endDateTime to a nicer format
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    const formattedStartDateTime = new Date(startDateTime).toISOString().slice(0,16);
    const formattedEndDateTime = new Date(endDateTime).toISOString().slice(0,16);
    // Create the container for the card
    const card = createEle('div', ['bg-gray-700', 'rounded-lg', 'shadow-lg', 'p-6']);

    

    const data = {
        scheduleID,
        startTime:startDateTime,
        endTime:endDateTime,
        desc:description
    }
    // Create and append the schedule number title
    const title = createEle('h3', ['text-2xl', 'font-bold', 'mb-4'], null, { innerText: `Awake Schedule #${scheduleCount}` });
    card.appendChild(title);
    scheduleCount++
    // Create and append the Awake From time with editable feature
    const awakeFrom = createEle('p', ['text-lg'], null, { innerHTML: `<strong>Awake From:</strong> <input type='datetime-local' value='${formattedStartDateTime}' class='bg-gray-800 text-white border border-gray-500 p-1 rounded-md cursor-pointer shadow-lg hover:bg-gray-700 focus:bg-gray-600 transition duration-300 ease-in-out'>` });
    awakeFrom.querySelector('input').addEventListener('change', (e) => {
        const dateValue = new Date(e.target.value);
        const formattedDate = new Date(
            dateValue.getTime() - dateValue.getTimezoneOffset() * 60000
        ).toISOString();        
        data['startTime'] = formattedDate
        postEdit(data);
    });
    card.appendChild(awakeFrom);

    // Create and append the Awake Until time with editable feature
    const awakeUntil = createEle('p', ['text-lg'], null, { innerHTML: `<strong>Awake Until:</strong> <input type='datetime-local' value='${formattedEndDateTime}' class='bg-gray-800 text-white border border-gray-500 p-1 rounded-md cursor-pointer shadow-lg hover:bg-gray-700 focus:bg-gray-600 transition duration-300 ease-in-out'>` });
    awakeUntil.querySelector('input').addEventListener('change', (e) => {
        const dateValue = new Date(e.target.value);
        const formattedDate = new Date(
            dateValue.getTime() - dateValue.getTimezoneOffset() * 60000
        ).toISOString();
        data['endTime'] = formattedDate;   
        postEdit(data);
    });
    card.appendChild(awakeUntil);

    // Create and append the Description with editable feature
    const desc = createEle('p', ['mt-4', 'text-lg', 'flex','gap-2'], null, { innerHTML: `<strong>Description:</strong> <textarea class='bg-gray-800 text-white border border-gray-500 p-2 rounded-md cursor-pointer shadow-lg hover:bg-gray-700 focus:bg-gray-600 transition duration-300 ease-in-out'>${description}</textarea>` });
    desc.querySelector('textarea').addEventListener('change', (e) => {
        data['desc'] = e.target.value
        postEdit(data);
    });
    card.appendChild(desc);

    return card;
}

async function createNewSchedule(startDateTime, endDateTime, description) {
    const scheduleContainer = document.querySelector('#schedule');

    const currentDateTime = new Date();
    const currentEndTime = new Date(currentDateTime.getTime() + 60 * 60 * 24 * 1000);
    
    // Format the datetime in ISO format for PHP strtotime
    const formattedStartTime = currentDateTime.toISOString();
    const formattedEndTime = currentEndTime.toISOString();
    
    
    const response = await postRequest('backend/create_schedule.php', { 
        startTime: formattedStartTime, 
        endTime: formattedEndTime, 
        desc: 'No Description' 
    });
    const scheduleID = response.scheduleID 
    scheduleContainer.appendChild(createScheduleCard(formattedStartTime, formattedEndTime, 'Edit Description',scheduleID));

}
document.addEventListener('DOMContentLoaded', async () => {
    const addScheduleButton = document.querySelector('#add-schedule');
    addScheduleButton.addEventListener('click', () => {
        createNewSchedule();
    });

    const shareButton = document.querySelector('#share');
    shareButton.addEventListener('click', async () => {
        const result = await postRequest('backend/share_admin.php', {}, null);
        if ('error' in result){
            alert(result.error)
            return;
        }
        else{
            alert(result.data)
        }
    });

    const scheduleContainer = document.querySelector('#schedule');
    const awakeTimeEle = document.querySelector('#time');
    const errorMessage = 'How dare you sleep! Disgusting.';
    var params = {errorMessage};
    
    
    if (limit) params['limit'] = limit;
    var schedule = await getRequest('backend/get_schedule.php', params, null, true);

    

    if (schedule.includes(errorMessage)){
        alert(errorMessage);
        schedule = schedule.substring(0, schedule.length-schedule.indexOf(errorMessage));
    }
    schedule = JSON.parse(schedule);
    if ('error' in schedule){
        alert(schedule.error);
        window.location.href = '?page=login';
        return;
    }
    
    const rows = schedule['rows'];
    for (let i = 0; i < rows.length; i++){
        scheduleContainer.appendChild(createScheduleCard( rows[i].startTime, rows[i].endTime, rows[i].desc,rows[i].scheduleID));
    }
    awakeTimeEle.innerHTML = schedule.awakeHours /60/60;

    
    
})