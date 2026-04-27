#include "philo.h"

static void	init_mutex(t_data *d)
{
	int	i;

	i = 0;
	while (i < d->num)
	{
		pthread_mutex_init(&d->forks[i], NULL);
		i++;
	}
	pthread_mutex_init(&d->print, NULL);
	pthread_mutex_init(&d->stop_mutex, NULL);
	pthread_mutex_init(&d->meal_mutex, NULL);
}

static void	init_philos(t_data *d)
{
	int	i;

	i = 0;
	while (i < d->num)
	{
		d->philos[i].id = i + 1;
		d->philos[i].eat_count = 0;
		d->philos[i].last_meal = ft_time();
		d->philos[i].left = &d->forks[i];
		d->philos[i].right = &d->forks[(i + 1) % d->num];
		d->philos[i].data = d;
		i++;
	}
}

void	init_data(t_data *d, int ac, char **av)
{
	d->num = ft_atoi(av[1]);
	d->time_die = ft_atoi(av[2]);
	d->time_eat = ft_atoi(av[3]);
	d->time_sleep = ft_atoi(av[4]);
	d->must_eat = -1;
	if (ac == 6)
		d->must_eat = ft_atoi(av[5]);
	d->stop = 0;
	d->forks = malloc(sizeof(pthread_mutex_t) * d->num);
	d->philos = malloc(sizeof(t_philo) * d->num);
	init_mutex(d);
	init_philos(d);
}

void	start_simulation(t_data *d)
{
	int			i;
	pthread_t	mon;

	d->start = ft_time();
	i = 0;
	while (i < d->num)
	{
		pthread_create(&d->philos[i].thread,
			NULL, routine, &d->philos[i]);
		i++;
	}
	pthread_create(&mon, NULL, monitor, d);
	i = 0;
	while (i < d->num)
	{
		pthread_join(d->philos[i].thread, NULL);
		i++;
	}
	pthread_join(mon, NULL);
}

int	main(int ac, char **av)
{
	t_data	d;

	if (ac != 5 && ac != 6)
		return (1);
	init_data(&d, ac, av);
	start_simulation(&d);
	destroy_mutex(&d);
	free_all(&d);
	return (0);
}