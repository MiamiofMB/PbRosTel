

async function saveToServer(btn_type) {
    try {

        elem = document.getElementById('pb_id_input').value
      const response = await fetch('/', {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({'pb_id':elem,'btn_type':btn_type}),
      });
      console.log(response.body)
      await response.json().then((value) => {
        window.location.href = value.re;
        });


    } catch (error) {
      console.error('Error: ', error);
    }
  }
async function saveToServer2(btn_type) {
    try {


      const response = await fetch(window.location.href, {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({'btn_type':btn_type}),
      });
      //const result = await response.statusText();
      //console.log(result['re'])
      console.log(response.body)
      //await response.json().then((value) => {
        //window.location.href = value.re;
        //});

      //window.location.href = window.location.href + '/giveout';
    } catch (error) {
      console.error('Error: ', error);
    }
  }
