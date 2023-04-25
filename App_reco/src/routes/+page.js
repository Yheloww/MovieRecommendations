
    export async function load({ fetch }) {
        const res = await fetch(
            'https://api.themoviedb.org/3/search/movie?api_key=0f19c042aac4b96dd9c50c70ff491332&query=batman'
        )
        console.log('reponse: ${res}')
        const data = await res.json();
        console.log(data.results);
        if (res.ok){
            return {
                props: { popular: data.results }
            };
        }
    }
