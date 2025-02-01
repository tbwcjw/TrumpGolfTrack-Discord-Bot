<p align="center">
    <h2 align="center">TrumpGolfTrack-Discord-Bot</h2>
<p align="center">
    A Discord bot written in Python that tracks Donald Trump's golf outings using Selenium to scrape <a href="https://trumpgolftrack.com/">https://trumpgolftrack.com/</a>, a nonaffiliate.
</p>
<p align="center">
<img width="50%" src="https://github.com/tbwcjw/TrumpGolfTrack-Discord-Bot/blob/main/example.png?raw=true">
<h4>Setup</h4>
<ul>
    <li>Add the token from <code>Settings > Bot > Token</code> to the <code>TOKEN=</code> line of config.py.</li>
    <li>Set the <code>CHROME_DRIVER_PATH</code> line of config.py to the full path of <code>chromedriver.exe</code>.
    <li>Under <code>Settings > Bot > Privileged Gateway Intents</code> turn on the following:
        <ul>
            <li>Presence Intent</li>
            <li>Message Content Intent</li>
        </ul>
    </li>
    <li>Under <code>Settings > Installation > Default Install Settings > Guild Install</code> set the following:
        <ul>
            <li>Scopes: <code>applications.commands</code>, <code>bot</code>.</li>
            <li>Permissions: <code>Read Message History</code>, <code>Send Messages</code>, <code>Use Slash Commands</code>.</li>
        </ul>
    <li>You can turn off <code>Public Bot</code> under <code>Settings > Bot > Public Bot</code>.
</ul>
<h4>TODO</h4>
<ul>
    <li>Set up and publish a docker container, for easy install.</li>
</ul>
<h4>Contribution</h4>
<p>Contribution is welcome! New features, bug fixes, internationalization. Submit your pull requests, thanks!</p>

