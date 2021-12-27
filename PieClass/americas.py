import pygal
wm = pygal.maps.world.World()
wm.title = 'High Level Threats'
wm.add('POI #1', ['ru', 'iq','dj','cn'])
wm.add('POI #2', ['ne', 'bw', 'et', 'ht', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
wm.add('POI #3', ['us', 'ee', 'us', 'uy', 'uz'])
wm.render()
wm.render_to_file('americas.svg')