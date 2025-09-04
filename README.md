<h1 align="center">Houdini Path Relinker</h1>
<div align="center">
  <a href="https://github.com/search?q=owner%3AParkerBritt+topic%3Ahoudini&type=repositories"><img src="https://cards.parkerbritt.com/badge?label=houdini&icon=houdini&color=FF4713"></a>
  <a href="https://github.com/ParkerBritt?tab=repositories&q=&type=&language=python&sort="><img src="https://cards.parkerbritt.com/badge?label=python&icon=python&color=3776AB"></a>
 </div>

<div align="justify">
 A tool to relink invalid absolute path parameters to valid $HIP paths. This is useful when continuing another artist's file, cleaning up paths in your own file, or moving your file from a different computer.
 This works for nodes in pretty much any Houdini context that references files, including lops and cops.
</div>


<br>Eg.<br>
```Z:/invalid/path/to/file.obj```<br>
turns into<br>
```$HIP/../file.obj```
