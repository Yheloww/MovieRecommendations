<script>
    import { onMount } from "svelte";
    let posts = []
    const headers = new Headers();
headers.append('Access-Control-Allow-Origin', '*');
headers.append('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
headers.append('Access-Control-Allow-Headers', 'Content-Type');

    onMount(async () => {
        const response = await fetch('http://localhost:8000/', 
        {
        headers: headers
        }).then(response => response.json())
        .then(result => posts = result); })

    let prefix;

    

  </script>
<main>
    <input placeholder="filter prefix" bind:value={prefix}>

    {#each posts as post (post.title)}
    <h2>{post.title} {post.year}</h2>
    <hr>
  {/each}
</main>


<style> 
    input {
        display: block;
		margin: 0 0 0.5em 0;
        size: 10em;
    }
</style>